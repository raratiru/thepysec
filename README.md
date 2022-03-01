[![Build Status](https://github.com/raratiru/thepysec/actions/workflows/python-package.yml/badge.svg)](https://github.com/raratiru/thepysec/actions)
[![Coverage Status](https://coveralls.io/repos/github/raratiru/thepysec/badge.svg?branch=master&service=github)](https://coveralls.io/github/raratiru/thepysec?branch=master)


A collection of tools that support a busy project based on Python >= 3.6.

John
----

John is the Battler. He will serve the necessary files needed to run thepysec.

Lia
---

Lia is here to take a detailed look at your strings.

* `pop_wsp`: Remove extra whitespace.
* `pre_slug`: Prepare a string to become a wise slug.
    * 'r33a!bc' -> 'r 33 abc'.
* `fast_pre_slug`: Prepare a string to become a fast slug.
    * 'r33a!bc' -> 'r 3 3 a bc'.
* `cap_sentence`: Carefully capitalize first letter and remove white space
    * "O'Connor is &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; INVITED to UK" -> "O'Connor Is Invited To UK"

Matina
------

Matina performs operations on django model instances

* `pop_i18n_wsp`: Apply `pop_wsp` for a list of fields in a given model instance.

Myriam
------

Myriam a mathematical kind of jelly roll.

* `validate_overlap`: Receives a list of DateRange or DateTimeRange and examines if contents overlap.


Thanos
------

Thanos is a Django test assistant

* `get_formset_alive`: Receives a formset class with data dictionary and returns a formset instance.


Otto
----

A pythonista who slightly bends the borders of the language

* `deep_getattr`: Dives in an object by performing successive getattrs for each word in a dotted string.
