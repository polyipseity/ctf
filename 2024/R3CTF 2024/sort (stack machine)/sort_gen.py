from pathlib import Path


COMP_AND_EXC = (
    [
        (0, 1),
        (2, 3),
        (4, 5),
        (6, 7),
        (8, 9),
        (10, 11),
        (12, 13),
        (14, 15),
        (16, 17),
        (18, 19),
        (20, 21),
        (22, 23),
        (24, 25),
        (26, 27),
        (28, 29),
    ],
    [
        (0, 2),
        (1, 3),
        (4, 6),
        (5, 7),
        (8, 10),
        (9, 11),
        (13, 15),
        (14, 16),
        (18, 20),
        (19, 21),
        (22, 24),
        (23, 25),
        (26, 28),
        (27, 29),
    ],
    [
        (0, 4),
        (1, 5),
        (2, 6),
        (3, 7),
        (8, 14),
        (9, 17),
        (10, 16),
        (12, 20),
        (13, 19),
        (15, 21),
        (22, 26),
        (23, 27),
        (24, 28),
        (25, 29),
    ],
    [
        (0, 8),
        (1, 9),
        (2, 14),
        (3, 17),
        (4, 10),
        (5, 11),
        (6, 16),
        (12, 26),
        (13, 23),
        (15, 27),
        (18, 24),
        (19, 25),
        (20, 28),
        (21, 29),
    ],
    [
        (1, 13),
        (2, 12),
        (3, 15),
        (4, 18),
        (5, 19),
        (6, 20),
        (7, 21),
        (8, 22),
        (9, 23),
        (10, 24),
        (11, 25),
        (14, 26),
        (16, 28),
        (17, 27),
    ],
    [
        (0, 4),
        (2, 8),
        (3, 13),
        (5, 9),
        (6, 22),
        (7, 23),
        (10, 12),
        (11, 15),
        (14, 18),
        (16, 26),
        (17, 19),
        (20, 24),
        (21, 27),
        (25, 29),
    ],
    [
        (0, 2),
        (1, 14),
        (3, 5),
        (4, 8),
        (9, 13),
        (11, 17),
        (12, 18),
        (15, 28),
        (16, 20),
        (21, 25),
        (24, 26),
        (27, 29),
    ],
    [
        (2, 4),
        (5, 9),
        (6, 14),
        (7, 13),
        (8, 10),
        (15, 23),
        (16, 22),
        (19, 21),
        (20, 24),
        (25, 27),
    ],
    [(6, 8), (7, 11), (10, 14), (12, 16), (13, 17), (15, 19), (18, 22), (21, 23)],
    [
        (4, 6),
        (7, 9),
        (8, 10),
        (11, 13),
        (12, 14),
        (15, 17),
        (16, 18),
        (19, 21),
        (20, 22),
        (23, 25),
    ],
    [
        (1, 8),
        (3, 18),
        (5, 20),
        (7, 22),
        (9, 24),
        (10, 12),
        (11, 26),
        (13, 15),
        (14, 16),
        (17, 19),
        (21, 28),
    ],
    [
        (1, 2),
        (3, 10),
        (5, 12),
        (7, 14),
        (9, 16),
        (11, 18),
        (13, 20),
        (15, 22),
        (17, 24),
        (19, 26),
        (27, 28),
    ],
    [
        (2, 4),
        (3, 6),
        (5, 8),
        (7, 10),
        (9, 12),
        (11, 14),
        (13, 16),
        (15, 18),
        (17, 20),
        (19, 22),
        (21, 24),
        (23, 26),
        (25, 27),
    ],
    [
        (3, 4),
        (5, 6),
        (7, 8),
        (9, 10),
        (11, 12),
        (13, 14),
        (15, 16),
        (17, 18),
        (19, 20),
        (21, 22),
        (23, 24),
        (25, 26),
    ],
)
TEMPLATE = R"""
DUP
DUP
PUSH (b - a) * 8
SHL
XOR
PUSH 255
PUSH b * 8
SHL
AND
PUSH 0
PUSH (b - a) * 8
SUB
DUP2
SWAP
SHL
OR
DUP2
DUP2
DUP2
XOR
GT
MUL
XOR
""".strip()

if __name__ == "__main__":
    Path("sort.txt").write_text(
        "\n".join(
            (
                TEMPLATE.replace("(b - a) * 8", str((b - a) * 8)).replace(
                    "b * 8", str(b * 8)
                )
                for x in COMP_AND_EXC
                for a, b in x
            )
        )
        + "\n"
    )