#!/usr/bin/bash
# this should be called from within docker to kick off a build
DISABLE_TELEMETRY=1
cd /app
echo ""
echo "============================================"
echo "Installing dependencies"
echo "============================================"
echo ""
python3 /app/airunner/dobuild.py
echo ""
echo "============================================"
echo "Build airunner for linux"
echo "============================================"
echo ""
DEV_ENV=0 AIRUNNER_ENVIRONMENT="prod" PYTHONOPTIMIZE=0 python3 -m PyInstaller --log-level=INFO --noconfirm  /app/airunner/build.airunner.linux.prod.spec 2>&1 | tee build.log
echo ""
echo "============================================"
echo "Deploying airunner to itch.io"
echo "============================================"
echo ""
chown -R 1000:1000 dist
LATEST_TAG=$(grep -oP '(?<=version=).*(?=,)' setup.py | tr -d "'")
echo "Latest tag: $LATEST_TAG"
echo $LATEST_TAG > ./dist/VERSION