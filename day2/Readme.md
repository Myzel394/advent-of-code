## [Link](https://adventofcode.com/2020/day/2)

## Task (part 1)

1. write a validity check for passwords, based on the given syntax
   `2-5 l: fllxf`
2. list the valid passwords
3. submit the len of (2.)

## Solution (part 1)

```
valid passwords: 660
invalid passwords: 340
```

## Task (part 2)

1. write a validity check for passwords, based on the given syntax
   `2-5 l: fllxf`
    - on the index of 2 needs to be either 'l' or anyother char, if there is an
      'l' the index 5 has to be anyother char or the password is invalid
2. list the valid passwords
3. submit the len of (2.)

## Solution (part 2)

```
valid passwords: 530
invalid passwords: 470
```
