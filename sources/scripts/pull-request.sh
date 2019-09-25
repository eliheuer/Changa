#!/bin/bash
set -e

prDir="~/Google/fonts/ofl/"
familyName="Changa"

echo "[INFO] Preparing a new $familyName pull request at $prDir"

cp fonts/vf/$familyName-VF.ttf ~/Google/fonts/ofl/changa/$familyName[wght].ttf

echo "[INFO] Done preparing $familyName pull request at $prDir"
