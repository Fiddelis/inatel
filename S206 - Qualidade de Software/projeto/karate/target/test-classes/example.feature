Feature: Teste da API de usuários

  Scenario: Criar um usuário
    Given url 'http://localhost:8080/api'
    And request { "name": "Lucas", "email": "lucas@example.com", "password": "1234" }
    When method POST
    Then status 200
    And match response == { "name": "Lucas", "email": "lucas@example.com", "password": "1234" }

  Scenario: Obter o usuário criado
    Given url 'http://localhost:8080/api'
    When method GET
    Then status 200
    And match response == { "name": "Lucas", "email": "lucas@example.com", "password": "1234" }

  Scenario: Tentar criar um usuário com dados nulos
    Given url 'http://localhost:8080/api'
    And request {}
    When method POST
    Then status 404
    And match response == { "erro": "usuario não pode ser nulo" }

  Scenario: Excluir o usuário
    Given url 'http://localhost:8080/api'
    When method DELETE
    Then status 200
    And match response == ""

  Scenario: Obter o usuário após exclusão
    Given url 'http://localhost:8080/api'
    When method GET
    Then status 404
    And match response == { "erro": "nenhum usuario encontrado" }