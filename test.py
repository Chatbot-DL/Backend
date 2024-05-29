import ollama

stream = ollama.chat(
    model='chatboot-game',
    messages=[{'role': 'user', 'content': 'raconte moi une histoire des jeu video pour apprendre la sommation dans 5 lignes'}],
    stream=True,
)

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)
