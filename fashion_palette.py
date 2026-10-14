
import random
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

PALETTES = {
    "elegant": {
        "Ivory": "#F5F0E8",
        "Charcoal": "#343434",
        "Burgundy": "#800020",
        "Taupe": "#A39483",
        "Gold": "#C5A253",
    },
    "romantic": {
        "Blush Pink": "#E8B4B8",
        "Dusty Rose": "#C08081",
        "Cream": "#FFF1DC",
        "Mauve": "#B784A7",
        "Soft Brown": "#9C7B70",
    },
    "minimalist": {
        "White": "#FFFFFF",
        "Light Grey": "#D9D9D9",
        "Stone": "#B5AA9A",
        "Black": "#202020",
        "Navy": "#253858",
    },
    "autumn": {
        "Rust": "#B55233",
        "Mustard": "#D4A72C",
        "Olive": "#777744",
        "Chocolate": "#59392B",
        "Cream": "#F2E5CC",
    },
    "winter": {
        "Ice Blue": "#C7DDF2",
        "Silver": "#C0C0C0",
        "Navy": "#172A4D",
        "Berry Red": "#9F2148",
        "Snow White": "#FAFAFF",
    },
    "spring": {
        "Sakura Pink": "#F4B6C2",
        "Mint Green": "#B8DCC8",
        "Lilac": "#C8B6E2",
        "Butter Yellow": "#F6E7A1",
        "Cream": "#FFF8E7",
    },
    "summer": {
        "Coral": "#F08080",
        "Ocean Blue": "#5DA9C7",
        "Lemon Yellow": "#F7E36D",
        "Terracotta": "#D97954",
        "Sand": "#E8D5B7",
    },
    "night": {
        "Midnight Blue": "#191B3A",
        "Moonlight": "#C8D0E8",
        "Plum": "#633B70",
        "Burgundy": "#800F2F",
        "Starlight": "#F4EDE1",
    },
    "day": {
        "Sky Blue": "#87CEEB",
        "Sunshine Yellow": "#FFD166",
        "White": "#FFFFFF",
        "Peach": "#FFB385",
        "Sage Green": "#A8BFA3",
    },
    "dawn": {
        "Rose Mist": "#E8A0B5",
        "Lavender": "#B7A5D5",
        "Apricot": "#F6B98B",
        "Horizon Blue": "#A8C5D8",
        "Pearl": "#FFF1E6",
    },
}


def generate_palette():
    print("\nAvailable fashion styles:")
    for style in PALETTES:
        print(f"- {style.title()}")

    style = input("\nChoose a style: ").strip().lower()

    if style not in PALETTES:
        print("Style not found. Choosing a random style.")
        style = random.choice(list(PALETTES.keys()))

    colors = PALETTES[style]

    fig, ax = plt.subplots(figsize=(10, 3))
    fig.patch.set_facecolor("#F8F5F0")
    ax.set_facecolor("#F8F5F0")

    for i, (name, hex_code) in enumerate(colors.items()):
        ax.add_patch(
            Rectangle((i, 0), 1, 1, color=hex_code)
        )
        ax.text(
            i + 0.5, -0.12, name,
            ha="center", va="top", fontsize=9
        )
        ax.text(
            i + 0.5, 0.5, hex_code,
            ha="center", va="center", fontsize=8,
            color="white" if i in (1, 2) else "black"
        )

    ax.set_xlim(0, len(colors))
    ax.set_ylim(-0.35, 1)
    ax.axis("off")

    plt.title(f"{style.title()} Fashion Palette", pad=15)
    plt.tight_layout()
    filename = f"{style}_fashion_palette.png"
    plt.savefig(filename, dpi=200, bbox_inches="tight")
    print(f"\nPalette saved as {filename}!")

    plt.show()


if __name__ == "__main__":
    generate_palette()
