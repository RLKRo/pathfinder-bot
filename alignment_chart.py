import matplotlib.pyplot as plt
import ast
import io


def alignment_chart(message: str) -> bytes:
    chars = ast.literal_eval(message)
    for char in chars:
        plt.scatter(*char[:2], label=char[2])
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    plt.hlines([-0.5, 0.5], [-1.5, -1.5], [1.5, 1.5])
    plt.vlines([-0.5, 0.5], [-1.5, -1.5], [1.5, 1.5])
    plt.xticks([-1, 0, 1], ['Lawful', 'Neutral', 'Chaotic'])
    plt.yticks([-1, 0, 1], ['Evil', 'Neutral', 'Good'])
    plt.legend()

    with io.BytesIO() as b:
        plt.savefig(b, format='png')
        plt.close()
        b.seek(0)
        return b.read()

