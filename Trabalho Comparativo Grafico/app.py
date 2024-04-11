import random
import matplotlib.pyplot as plt
import time

def gereador_de_vetor(tamanho): # -> Cria um vetor com tamanho e valores diferentes.
    vetor = []
    while len(vetor) < tamanho:
        novo_Num = random.randint(0, 100000)
        if novo_Num not in vetor:
            vetor.append(novo_Num)
    return vetor


#-----------------------------------------------------------------------------#
def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
#-----------------------------------------------------------------------------#
def bubblesort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
#-----------------------------------------------------------------------------#
def selectionsort(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
#-----------------------------------------------------------------------------#
def quicksort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quicksort(left) + middle + quicksort(right)
#-----------------------------------------------------------------------------#
def mergesort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]

        mergesort(left_half)
        mergesort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1
#-----------------------------------------------------------------------------#


# Verifica o tempo de execucao.
def tempo_de_medida_xecucao(algo):
    sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000]  # Example sizes
    execution_times = []
    for size in sizes:
        vetor = gereador_de_vetor(size)
        start_time = time.time()
        algo(vetor)
        end_time = time.time()
        execution_times.append(end_time - start_time)
    return sizes, execution_times

def graficoSeparado():
    fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(14, 8))

    sizes, execution_times = tempo_de_medida_xecucao(insertionSort)
    axes[0, 0].plot(sizes, execution_times, label="Insertion Sort", lw=2)
    axes[0, 0].set_title("Insertion Sort")
    axes[0, 0].set_xlabel("Tamanho do vetor")
    axes[0, 0].set_ylabel("Tempo em segundos")

    sizes, execution_times = tempo_de_medida_xecucao(bubblesort)
    axes[0, 1].plot(sizes, execution_times, label="Bubble Sort", lw=2)
    axes[0, 1].set_title("Bubble Sort")
    axes[0, 1].set_xlabel("Tamanho do vetor")
    axes[0, 1].set_ylabel("Tempo em segundos")

    sizes, execution_times = tempo_de_medida_xecucao(selectionsort)
    axes[0, 2].plot(sizes, execution_times, label="Selection Sort", lw=2)
    axes[0, 2].set_title("Selection Sort")
    axes[0, 2].set_xlabel("Tamanho do vetor")
    axes[0, 2].set_ylabel("Tempo em segundos")

    sizes, execution_times = tempo_de_medida_xecucao(quicksort)
    axes[1, 0].plot(sizes, execution_times, label="Quick Sort", lw=2)
    axes[1, 0].set_title("Quick Sort")
    axes[1, 0].set_xlabel("Tamanho do vetor")
    axes[1, 0].set_ylabel("Tempo em segundos")

    sizes, execution_times = tempo_de_medida_xecucao(mergesort)
    axes[1, 1].plot(sizes, execution_times, label="Merge Sort", lw=2)
    axes[1, 1].set_title("Merge Sort")
    axes[1, 1].set_xlabel("Tamanho do vetor")
    axes[1, 1].set_ylabel("Tempo em segundos")

    # Remove o subplot vazio
    fig.delaxes(axes[1, 2])

    plt.tight_layout()
    plt.show()

def graficoUnificado():
    sizes, execution_times = tempo_de_medida_xecucao(insertionSort)
    plt.plot(sizes, execution_times, label="Insertion Sort", lw=2)

    sizes, execution_times = tempo_de_medida_xecucao(bubblesort)
    plt.plot(sizes, execution_times, label="Bubble Sort", lw=2)

    sizes, execution_times = tempo_de_medida_xecucao(selectionsort)
    plt.plot(sizes, execution_times, label="Selection Sort", lw=2)

    sizes, execution_times = tempo_de_medida_xecucao(quicksort)
    plt.plot(sizes, execution_times, label="Quick Sort", lw=2)

    sizes, execution_times = tempo_de_medida_xecucao(mergesort)
    plt.plot(sizes, execution_times, label="Merge Sort", lw=2)

    plt.grid(True)
    plt.title("Sort Algorithms Comparison")
    plt.xlabel("Tamanho do vetor")
    plt.ylabel("Tempo em segundos")
    plt.legend()
    plt.show()


# Menu para oferecer as duas opções de visualização.
while True:
    def menu():
        print("""
            Escolha uma das opcoes:
            [1] - Ver graficos de forma separada.
            [2] - Ver graficos de forma unificada.
            [3] - Sair do programa.
            """)
        answer = int(input())
        if answer == 1:
            graficoSeparado()
        if answer == 2:
            graficoUnificado()
        if answer == 3:
            pass
        else:
            print("""
                Resposta errada.
                Tente novamente.
                """)
            menu()
    break

menu()