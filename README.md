[![Build Status](https://github.com/raratiru/thepysec/actions/workflows/python-package.yml/badge.svg)](https://github.com/raratiru/thepysec/actions)
[![Coverage Status](https://coveralls.io/repos/github/raratiru/thepysec/badge.svg?branch=master&service=github)](https://coveralls.io/github/raratiru/thepysec?branch=master)


A collection of tools that support a busy project based on Python >= 3.8.

John
----

John is the Battler. He will serve the necessary files needed to run thepysec.

Lia
---

Lia is here to take a detailed look at your strings.

* [`pop_wsp`](https://github.com/raratiru/thepysec/blob/571cf49798e571f542c5ec65f45cf62ec5262399/thepysec/lia.py#L19): Remove extra whitespace.
* [`pre_slug`](https://github.com/raratiru/thepysec/blob/571cf49798e571f542c5ec65f45cf62ec5262399/thepysec/lia.py#L87): Prepare a string to become a wise slug.
    * 'r33a!bc' -> 'r 33 abc'.
* [`fast_pre_slug`](https://github.com/raratiru/thepysec/blob/571cf49798e571f542c5ec65f45cf62ec5262399/thepysec/lia.py#L23): Prepare a string to become a fast slug.
    * 'r33a!bc' -> 'r 3 3 a bc'.
* [`cap_sentence`](https://github.com/raratiru/thepysec/blob/571cf49798e571f542c5ec65f45cf62ec5262399/thepysec/lia.py#L141): Carefully capitalize first letter and remove white space
    * "O'Connor is &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; INVITED to UK" -> "O'Connor Is Invited To UK"

Matina
------

Matina performs operations on django model instances

* [`pop_i18n_wsp`](https://github.com/raratiru/thepysec/blob/571cf49798e571f542c5ec65f45cf62ec5262399/thepysec/matina.py#L18): Apply `pop_wsp` for a list of fields in a given model instance.

Myriam
------

Myriam a mathematical kind of jelly roll.

* [`validate_overlap`](https://github.com/raratiru/thepysec/blob/571cf49798e571f542c5ec65f45cf62ec5262399/thepysec/myriam.py#L16): Receives a list of DateRange or DateTimeRange and examines if contents overlap.


Thanos
------

Thanos is a Django test assistant

* [`get_formset_alive`](https://github.com/raratiru/thepysec/blob/571cf49798e571f542c5ec65f45cf62ec5262399/thepysec/thanos.py#L16): Receives a formset class with data dictionary and returns a formset instance.


Otto
----

A pythonista who slightly bends the borders of the language

* [`deep_getattr`](https://github.com/raratiru/thepysec/blob/571cf49798e571f542c5ec65f45cf62ec5262399/thepysec/otto.py#L8): Dives in an object by performing successive getattrs for each word in a dotted string.
* [`deep_get`](https://github.com/raratiru/thepysec/blob/4ee944291b832beeb75d6d22dd0a3bc045c108de/thepysec/otto.py#L22): Dives in a dictionary by performing successive getats for each word in a dotted string.
