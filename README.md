# Quadratic Formula

This is a python command line interface which allows you to solve a quadratic equation.

## How to Run

Assuming you have python installed:

```
python main.py a=1 b=5 c = 6
```

This should give us `x = -3` and `x = -2`

### What if you don't have python installed?

Use docker!

```
docker run -v ${pwd}:/app -w /app python:3.9 python main.py a=1 b=5 c=6
```
