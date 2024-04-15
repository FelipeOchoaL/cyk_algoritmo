def cky(grammar, word):
    n = len(word)
    dp = [[set() for j in range(n + 1)] for _ in range(n + 1)]

    for i, letter in enumerate(word):
        for key, values in grammar.items():
            if letter in values:
                dp[i][i + 1].add(key)

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length
            for k in range(i + 1, j):
                for key, values in grammar.items():
                    possible_combinations = {a + b for a in dp[i][k] for b in dp[k][j]}
                    matching_productions = possible_combinations.intersection(values)
                    if matching_productions:
                        dp[i][j].add(key)

    return 'S' in dp[0][n]

with open('test_cky.in', 'r') as file:
    num_cases = int(file.readline().strip())

    for _ in range(num_cases):
        line = file.readline().strip()
        if not line:
            break
        non_terminals = int(line[0])
        num_strings = int(line[2])

        grammar = {}
        for _ in range(non_terminals):
            line = file.readline().strip()
            key, *productions = line.split()
            grammar[key] = set(productions)

        #num_strings = int(file.readline().strip())  # Leemos el número de cadenas a analizar
        strings_to_test = [file.readline().strip() for _ in range(num_strings)]

        print(f"Grammar: {grammar}")

        for test_string in strings_to_test:
            result_message = "Accepted" if cky(grammar, test_string) else "Rejected"
            print(f"String '{test_string}' is {result_message}")
