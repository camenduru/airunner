from PyQt6.QtCore import QPoint
from airunner.history import History


class HistoryMixin:
    history = None
    window = None
    canvas = None

    def initialize(self):
        self.history = History()

    def undo_new_layer(self, previous_event):
        layers = self.ui.layer_widget.get_layers_copy()
        self.ui.layer_widget.layers = previous_event["layers"]
        self.ui.layer_widget.current_layer_index = previous_event["layer_index"]
        previous_event["layers"] = layers
        return previous_event

    def undo_move_layer(self, previous_event):
        layer_order = []
        for layer in self.ui.layer_widget.layers:
            layer_order.append(layer.uuid)
        self.resort_layers(previous_event)
        previous_event["layer_order"] = layer_order
        self.history.undone_history.append(previous_event)
        self.ui.layer_widget.current_layer_index = previous_event["layer_index"]
        return previous_event

    def undo_delete_layer(self, previous_event):
        layers = self.ui.layer_widget.get_layers_copy()
        self.ui.layer_widget.layers = previous_event["layers"]
        self.ui.layer_widget.current_layer_index = previous_event["layer_index"]
        previous_event["layers"] = layers
        return previous_event

    def undo_draw(self, previous_event):
        index = previous_event["layer_index"]
        lines = previous_event["lines"]
        previous_event["lines"] = self.ui.layer_widget.layers[index].lines.copy()
        self.ui.layer_widget.layers[index].lines = lines
        return previous_event

    def undo_erase(self, previous_event):
        # add lines to layer
        lines = previous_event["lines"]
        images = previous_event["images"]
        index = previous_event["layer_index"]
        previous_event["lines"] = self.ui.layer_widget.layers[index].lines
        previous_event["images"] = self.canvas.image_data_copy(index)
        self.ui.layer_widget.layers[index].lines = lines
        self.ui.layer_widget.layers[index].image_data = images
        return previous_event

    def undo_set_image(self, previous_event):
        images = previous_event["images"]
        layer_index = previous_event["layer_index"]
        previous_event["images"] = self.canvas.image_data_copy(layer_index)
        self.ui.layer_widget.layers[previous_event["layer_index"]].image_data = images
        return previous_event

    def undo_apply_filter(self, previous_event):
        images = previous_event["images"]
        index = previous_event["layer_index"]
        previous_event["images"] = self.canvas.image_data_copy(index)
        self.ui.layer_widget.layers[index].image_data = images
        return previous_event

    def undo_add_widget(self, previous_event):
        widets = previous_event["widgets"]
        previous_event["widgets"] = self.ui.layer_widget.layers[previous_event["layer_index"]].widgets
        self.ui.layer_widget.layers[previous_event["layer_index"]].widgets = widets
        return previous_event

    def undo_rotate(self, previous_event):
        images = previous_event["images"]
        index = previous_event["layer_index"]
        previous_event["images"] = self.canvas.image_data_copy(index)
        self.ui.layer_widget.layers[index].image_data = images
        return previous_event

    def undo(self):
        if len(self.history.event_history) == 0:
            return
        previous_event = self.history.event_history.pop()
        event_name = previous_event["event"]
        if event_name == "draw":
            previous_event = self.undo_draw(previous_event)
        elif event_name == "erase":
            previous_event = self.undo_erase(previous_event)
        elif event_name == "new_layer":
            if len(self.ui.layer_widget.layers) == 1:
                self.history.event_history.append(previous_event)
                return
            previous_event = self.undo_new_layer(previous_event)
        elif event_name == "move_layer":
            self.undo_move_layer(previous_event)
        elif event_name == "delete_layer":
            self.undo_delete_layer(previous_event)
        elif event_name == "set_image":
            self.undo_set_image(previous_event)
        elif event_name == "add_widget":
            self.undo_add_widget(previous_event)
        elif event_name == "apply_filter":
            self.undo_apply_filter(previous_event)
        elif event_name == "rotate":
            self.undo_rotate(previous_event)
        self.history.undone_history.append(previous_event)
        self.ui.layer_widget.show_layers()
        self.canvas.update()

    def redo_draw(self, undone_event):
        lines = undone_event["lines"]
        undone_event["lines"] = self.ui.layer_widget.layers[undone_event["layer_index"]].lines
        self.ui.layer_widget.layers[undone_event["layer_index"]].lines = lines
        return undone_event

    def redo_erase(self, undone_event):
        lines = undone_event["lines"]
        images = undone_event["images"]
        layer_index = undone_event["layer_index"]
        undone_event["lines"] = self.ui.layer_widget.layers[layer_index].lines.copy()
        undone_event["images"] = self.canvas.image_data_copy(layer_index)
        self.ui.layer_widget.layers[undone_event["layer_index"]].lines = lines
        self.ui.layer_widget.layers[undone_event["layer_index"]].image_data = images
        return undone_event

    def redo_set_image(self, undone_event):
        images = undone_event["images"]
        layer_index = undone_event["layer_index"]
        current_image_root_point = QPoint(self.canvas.image_root_point.x(), self.canvas.image_root_point.y())
        current_image_pivot_point = QPoint(self.canvas.image_pivot_point.x(), self.canvas.image_pivot_point.y())
        undone_event["images"] = self.canvas.image_data_copy(layer_index)
        undone_event["previous_image_root_point"] = current_image_root_point
        undone_event["previous_image_pivot_point"] = current_image_pivot_point
        self.ui.layer_widget.layers[undone_event["layer_index"]].image_data = images
        return undone_event

    def redo_add_widget(self, undone_event):
        # add widget
        widgets = undone_event["widgets"]
        undone_event["widgets"] = self.ui.layer_widget.layers[undone_event["layer_index"]].widgets
        self.ui.layer_widget.layers[undone_event["layer_index"]].widgets = widgets
        return undone_event

    def redo_new_layer(self, undone_event):
        layers = self.ui.layer_widget.get_layers_copy()
        self.ui.layer_widget.layers = undone_event["layers"]
        self.ui.layer_widget.current_layer_index = undone_event["layer_index"]
        undone_event["layers"] = layers
        return undone_event

    def redo_move_layer(self, undone_event):
        layer_order = []
        for layer in self.ui.layer_widget.layers:
            layer_order.append(layer.uuid)
        self.resort_layers(undone_event)
        undone_event["layer_order"] = layer_order
        self.ui.layer_widget.current_layer_index = undone_event["layer_index"]
        return undone_event

    def redo_delete_layer(self, undone_event):
        layers = self.ui.layer_widget.get_layers_copy()
        self.ui.layer_widget.layers = undone_event["layers"]
        self.ui.layer_widget.current_layer_index = undone_event["layer_index"]
        undone_event["layers"] = layers
        return undone_event

    def redo_apply_filter(self, previous_event):
        images = previous_event["images"]
        index = previous_event["layer_index"]
        previous_event["images"] = self.canvas.image_data_copy(index)
        self.ui.layer_widget.layers[index].image_data = images
        return previous_event

    def redo_rotate(self, undone_event):
        images = undone_event["images"]
        layer_index = undone_event["layer_index"]
        undone_event["images"] = self.canvas.image_data_copy(layer_index)
        self.ui.layer_widget.layers[undone_event["layer_index"]].image_data = images
        return undone_event

    def redo(self):
        if len(self.history.undone_history) == 0:
            return
        undone_event = self.history.undone_history.pop()
        event_name = undone_event["event"]
        if event_name == "draw":
            undone_event = self.redo_draw(undone_event)
        elif event_name == "erase":
            undone_event = self.redo_erase(undone_event)
        elif event_name == "new_layer":
            undone_event = self.redo_new_layer(undone_event)
        elif event_name == "move_layer":
            undone_event = self.redo_move_layer(undone_event)
        elif event_name == "delete_layer":
            undone_event = self.redo_delete_layer(undone_event)
        elif event_name == "set_image":
            undone_event = self.redo_set_image(undone_event)
        elif event_name == "add_widget":
            undone_event = self.redo_add_widget(undone_event)
        elif event_name == "apply_filter":
            undone_event = self.redo_apply_filter(undone_event)
        elif event_name == "rotate":
            undone_event = self.redo_rotate(undone_event)
        self.history.event_history.append(undone_event)
        self.ui.layer_widget.show_layers()
        self.canvas.update()

    def resort_layers(self, event):
        layer_order = event["layer_order"]
        # rearrange the current layers to match the layer order before the move
        sorted_layers = []
        for uuid in layer_order:
            for layer in self.ui.layer_widget.layers:
                if layer.uuid == uuid:
                    sorted_layers.append(layer)
                    break
        self.ui.layer_widget.layers = sorted_layers

    def clear_history(self):
        self.history.clear()
