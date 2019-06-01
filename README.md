[![Build Status](https://travis-ci.org/raratiru/thepysec.svg?branch=master)](https://travis-ci.org/raratiru/thepysec)
[![Coverage Status](https://coveralls.io/repos/github/raratiru/thepysec/badge.svg?branch=master&service=github)](https://coveralls.io/github/raratiru/thepysec?branch=master)


A collection of tools that support a busy project based on Python >= 3.6.

John
----

John is the Battler. He will serve the necessary files needed to run thepysec.

Lia
---

Lia is here to take a detailed look at your strings.

* `strings.pop_wsp`: Remove extra whitespace.
* `strings.pop_i18n_wsp`: Remove extra whitespace from each field of django-translated-fields
* `strings.pre_slug`: Prepare a string to become a wise slug. 'r33a!bc' -> 'r 33 abc'
* `strings.fast_pre_slug`: Prepare a string to become a fast slug. 'r33a!bc' -> 'r 3 3 a bc'