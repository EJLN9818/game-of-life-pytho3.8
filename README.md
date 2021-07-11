# Conway's Game of Life
A Python implementation of Conway's Game of Life with pygame module.


## Rules
The rules, which compare the behavior of the automaton to real life, can be condensed into the following:
1. Any live cell with two or three live neighbours survives.
2. Any dead cell with three live neighbours becomes a live cell.
3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.

The initial pattern constitutes the seed of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed; births and deaths occur simultaneously, and the discrete moment at which this happens is sometimes called a tick. Each generation is a pure function of the preceding one. The rules continue to be applied repeatedly to create further generations.

## Features
| Command | Description | Values |
| - | ------------ | - |
| `F1` | Show / Hide in Game Menu |
| `<space>` | Play / Pause |
| `c` | New Cell Color | RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN |
| `g` | Show / Hide Grid |
| `+` \| `-` | Increase / Decrease Generations Per Second | 1-30 |
| `r` | Randomize new cells |
| `t` | Number of Tiles in Game | 16x12 (192), 32x24 (768), 64x48 (3072), 128x96 (12288)
| `<LMB>` | Turn On Dead Cell |
| `<RMB>` | Turn Off Alive Cell |
| `e` | Reset Game |
| `<ESC>` \| `q` | Quit Game |

- Cell becomes brighter with every generation that it survives until it turns completely white (after 51 generations).
- Implementation considers the left and right edges of the field to be stitched together, and the top and bottom edges also, yielding a toroidal array.

## Execute
python3.8 game-of-life.py
