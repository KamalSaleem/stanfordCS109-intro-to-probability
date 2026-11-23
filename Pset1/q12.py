{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "gpuType": "T4"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    },
    "accelerator": "GPU"
  },
  "cells": [
    {
      "cell_type": "code",
      "source": [
        "import random\n",
        "\n",
        "def win(x, y):\n",
        "  if y > x:\n",
        "    return True\n",
        "  elif y == x:\n",
        "    return None\n",
        "  return False\n",
        "\n",
        "def game():\n",
        "  x = 0\n",
        "  y = 0\n",
        "  sum = 0\n",
        "  while sum <= 100:\n",
        "    x = random.randint(1, 100)\n",
        "    sum += x\n",
        "  while sum <= 200:\n",
        "    y = random.randint(1, 100)\n",
        "    sum += y\n",
        "\n",
        "  return x, y\n",
        "\n",
        "x_wins = 0\n",
        "y_wins = 0\n",
        "for i in range(1000000):\n",
        "  x, y = game()\n",
        "  if win(x, y) == True:\n",
        "    y_wins += 1\n",
        "  elif win(x, y) == False:\n",
        "    x_wins += 1\n",
        "\n",
        "draws = i+1 - x_wins - y_wins\n",
        "prob_x = x_wins / (i+1)\n",
        "prob_y = y_wins / (i+1)\n",
        "prob_d = draws / (i+1)\n",
        "\n",
        "print(f\"the probability of x winning is {prob_x:.3f}\")\n",
        "print(f\"the probability of y winning is {prob_y:.3f}\")\n",
        "print(f\"the probability of a draw {prob_d:.3f}\")\n",
        "print(f\"total games: {i+1}\")\n",
        "print(f\"x won: {x_wins}\")\n",
        "print(f\"y won: {y_wins}\")\n",
        "print(f\"draws : {draws}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7mBuxQnq9-hQ",
        "outputId": "8151a02a-8116-40ec-ef10-efd81a9c8569"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "the probability of x winning is 0.466\n",
            "the probability of y winning is 0.522\n",
            "the probability of a draw 0.012\n",
            "total games: 1000000\n",
            "x won: 466400\n",
            "y won: 521661\n",
            "draws : 11939\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "81rmmpeT-fLV"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
