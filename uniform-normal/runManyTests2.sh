#!/usr/bin/env bash
python3 RunTests.py 4 100 .01 0 4_100_01_normal &
python3 RunTests.py 4 100 .055 0 4_100_055_normal &
python3 RunTests.py 4 100 .1 0 4_100_1_normal &
python3 RunTests.py 8 100 .01 0 8_100_01_normal &
python3 RunTests.py 8 100 .055 0 8_100_055_normal &
python3 RunTests.py 8 100 .1 0 8_100_1_normal &
python3 RunTests.py 16 100 .01 0 16_100_01_normal &
python3 RunTests.py 16 100 .055 0 16_100_055_normal &
python3 RunTests.py 16 100 .1 0 16_100_1_normal &
python3 RunTests.py 32 100 .01 0 32_100_01_normal &
python3 RunTests.py 32 100 .055 0 32_100_055_normal &
python3 RunTests.py 32 100 .1 0 32_100_1_normal &
python3 RunTests.py 4 1000 .01 0 4_1000_01_normal &
python3 RunTests.py 4 1000 .055 0 4_1000_055_normal &
python3 RunTests.py 4 1000 .1 0 4_1000_1_normal &
python3 RunTests.py 8 1000 .01 0 8_1000_01_normal &
python3 RunTests.py 8 1000 .055 0 8_1000_055_normal &
python3 RunTests.py 8 1000 .1 0 8_1000_1_normal &
python3 RunTests.py 16 1000 .01 0 16_1000_01_normal &
python3 RunTests.py 16 1000 .055 0 16_1000_055_normal &
python3 RunTests.py 16 1000 .1 0 16_1000_1_normal &
python3 RunTests.py 32 1000 .01 0 32_1000_01_normal &
python3 RunTests.py 32 1000 .055 0 32_1000_055_normal &
python3 RunTests.py 32 1000 .1 0 32_1000_1_normal &