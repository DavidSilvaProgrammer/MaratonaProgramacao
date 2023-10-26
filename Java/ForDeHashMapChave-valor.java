HashMap<String, Integer> idadePorNome = new HashMap<>();
idadePorNome.put("Alice", 25);
idadePorNome.put("Bob", 30);
idadePorNome.put("Carol", 22);

for (Map.Entry<String, Integer> entrada : idadePorNome.entrySet()) {
    System.out.println(entrada.getKey() + " tem " + entrada.getValue() + " anos.");
}
