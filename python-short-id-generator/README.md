
# Short ID Generator in Python

Source Code for **[Generate Short Url-Friendly Unique ID in Python](http://yewei.io/generate-short-id-python/)**


## Content

* **requirements.txt** - `pip install -r requirements.txt`
* **short_id_v0.py** - Version 0: Base62-Encoded UUID1
* **short_id_v1.py** - Version 1: Half Unshuffled UUID1
* **short_id_v2.py** - Version 2: Shuffled XOR UUID1
* **short_id_v3.py** - Version 3: Shuffled XOR UUID4
* **short_id_v4.py** - Version 4: Urandom
* **short_id_v5.py** - Version 5: Base62-Encoded Urandom
* **run_all.py** - One-click to run all versions once
* **count_distribution.py** - Get probability distribution of ID length
* **detect_collision.py** - Check how often a collision occurs
* **measure_time_cost.py** - Measure execution times of v0~4
* **measure_time_cost2.py** - Measure execution times of v4 & v5
* **verify_base62.py** - Verify if Base62 encoder is the same in v4 & v5
* **compress_right.py** - Implementation of [Parallel Bit Extract (PEXT)](https://en.wikipedia.org/wiki/Bit_Manipulation_Instruction_Sets#Parallel_bit_deposit_and_extract) instruction
