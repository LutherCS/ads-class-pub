# Animal Kingdom

Use the principles of object-oriented programming and implement the missing functionality of the following classes.

Classes `Animal`, `Penguin`, `Canine`, `Feline`, and `HouseCat` are implemented. You need to complete the other 5 classes in the following hierarchy:

![Animal kingdom](zoo.png)

You should take advantage of inheritance and call `super()` wherever applicable. See the test file for details of the expected output and exact return values.

1. Complete class `Bird`
   - abstract (cannot be instantiated)
   - extends `Animal`
   - has boolean data attribute `_flying`
1. Complete class `Mammal`
   - abstract (cannot be instantiated)
   - extends `Animal`
   - has data attribute `_habitat` that must be _Land_, _Sea_, _Air_, or _Tree_
1. Complete class `Parrot`
   - extends `Bird`
   - all parrots are flying birds
   - has boolean data attribute `_talking`
1. Complete class `Dog`
   - extends `Canine`
   - all dogs live on _Land_
   - all dogs make _Woof!_ sound
1. Complete class `BobCat`
   - extends `Feline`

## What to do

- Read _src/exercises/zoo/description.md_ (this file).
- Modify _src/exercises/zoo/zoo_classes.py_.
- Run _src/exercises/zoo/zoo_main.py_.

```bash
python3 src/exercises/zoo/zoo_main.py
```

- Compare your output to that provided in _tests/exercises/zoo/zoo_output.txt_.
- Test your implementation.

```bash
python -m pytest tests/exercises/zoo/test_zoo.py
```
