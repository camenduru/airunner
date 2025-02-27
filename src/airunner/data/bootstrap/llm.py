seed_data = {
    "seq2seq": {
        "generator_settings": {
            "top_p": 90,
            "max_length": 1024,
            "repetition_penalty": 100,
            "min_length": 10,
            "k": 0,
            "length_penalty": 100,
            "num_beams": 1,
            "ngram_size": 0,
            "temperature": 100,
            "sequences": 1,
            "top_k": 0,
            "seed": 0,
            "do_sample": False,
            "early_stopping": False,
            "random_seed": False,
            "model_version": ""
        },
        "model_versions": [
            "google/flan-t5-xxl",
            "google/flan-t5-xl",
            "google/flan-t5-large",
            "google/flan-t5-small",
            "google/flan-t5-base"
        ]
    },
    "casuallm": {
        "generator_settings": {
            "top_p": 90,
            "max_length": 4096,
            "repetition_penalty": 100,
            "min_length": 0,
            "k": 0,
            "length_penalty": 100,
            "num_beams": 1,
            "ngram_size": 0,
            "temperature": 100,
            "sequences": 4,
            "top_k": 0,
            "seed": 0,
            "do_sample": False,
            "early_stopping": False,
            "random_seed": False,
            "model_version": [
                "meta-llama/Llama-2-7b-hf",
                "meta-llama/Llama-2-7b-chat-hf",
                "mistralai/Mistral-7B-v0.1",
                "mistralai/Mistral-7B-Instruct-v0.1",
                "gpt2-xl",
                "gpt2-large",
            ]
        }
    }
}