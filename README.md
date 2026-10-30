*This project has been created as part of the 42 curriculum by mbouyer.*

RAG:

## Description

## Instructions

### Installation

```bash
uv sync
```

or

``` bash
make install
```

### Running the program

```bash
uv run python3 -m src
```

or 

``` bash
make run
```


### Makefile targets

| Target  | Action  |
| --- | --- |
| `install` | Install dependencies with `uv sync` |
| `run` | Run the program |
| `debug` | Run the program with pdb (debug mode)  |
| `clean` | Remove Python caches  |
| `lint`  | Run flake8 and mypy |
| `lint-strict` | Run flake8 and mypy --strict |


## Resources

- [w3school](https://www.w3schools.com/) - practising Python exercises: classes, modules, regex, algorithms comparison, etc.
- [Stephane Robert's blog](https://blog.stephane-robert.info) - Deep explanation of the regex with examples.

### AI usage

Claude (Anthropic) was used throughout this project as a learning and organizational aid:
- Breaking the project down into steps
- Reviewing code and identifying bugs(type errors, logic errors)

All code was written, understood and tested by me; AI was not used to generate unreviewed code.

## Additional sections

### System architecture: Describe your RAG pipeline components and how they interact

### Chunking strategy: Explain your approach to document segmentation

### Retrieval method: Detail the retrieval algorithm and ranking mechanism

### Performance analysis: Discuss recall@k scores and system performance

### Design decisions: Explain key implementation choices

### Challenges faced: Document difficulties encountered and solutions

### Example usage: Provide clear examples of running your system