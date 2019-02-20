# Animal Kingdom

Use the principles of object-oriented programming and implement the missing functionality of the following classes.

Classes `Animal`, `Penguin`, `Canine`, `Feline`, and `HouseCat` are implemented. You need to complete the other 5 classes in the following hierarchy:

![Animal kingdom](zoo.png)

You should take advantage of inheritance and call `super()` wherever applicable.

1. Complete class `Bird`
    - extends `Animal`
    - has boolean data attribute `_flying`
1. Complete class `Mammal`
    - extends `Animal`
    - has data attribute `_habitat` that can be **Land**, **Sea**, **Air**, or **Tree**
1. Complete class `Parrot`
    - extends `Bird`
    - has boolean data attribute `_talking`
1. Complete class `Dog`
    - extends `Canine`
    - all dogs live on **Land**
    - all dogs make **Woof!** sound
1. Complete class `BobCat`
    - extends `Feline`

## What to do

- Read *src/exercises/zoo/description.md* (this file).
- Modify *src/exercises/zoo/zoo_classes.py*.
- Run the exercise driver file.

```bash
python3 src/exercises/zoo/zoo_main.py
```

- Compare your output to that provided in *tests/exercises/zoo/zoo_output.txt*.
- Test your implementation.

```bash
python3 -m pytest tests/exercises/zoo/test_zoo.py
```
