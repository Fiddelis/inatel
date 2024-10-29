/// <reference = cypress>

    describe("4 positivos, 2 negativo", () => {
        it("teste de busca com sucesso(positivo)", () => {
            cy.visit("https://www.wikipedia.org/")
            cy.get("#searchInput").type("Airton Senna")
            cy.get('[href="https://pt.wikipedia.org/wiki/Ayrton_Senna"]').click()
            cy.get('.mw-page-title-main').should("have.text", "Ayrton Senna")
        })
        
        it("teste de mudar idioma com sucesso(positivo)", () => {
            cy.visit("https://www.wikipedia.org/")
            cy.get('.svg-arrow-down-blue').click()
            cy.get(':nth-child(2) > ul > :nth-child(3) > a').click()
            cy.get('#Welcome_to_Wikipedia').should("have.text", "Welcome to Wikipedia")
        })

        it("teste de retornar para pagina inicial com sucesso(positivo)", () => {
            cy.visit("https://www.wikipedia.org/")
            cy.get("#searchInput").type("Gato")
            cy.get('[href="https://pt.wikipedia.org/wiki/Gato"]').click()
            cy.get('.mw-logo').click()
            cy.get('.hp-welkom-1').should("have.text", "Boas-vindas à Wikipédia,")
        })

        it("teste da pagina de editar artigo com sucesso(positivo)", () => {
            cy.visit("https://www.wikipedia.org/")
            cy.get("#searchInput").type("Alan Turing")
            cy.get('[href="https://pt.wikipedia.org/wiki/Alan_Turing"]').click()
            cy.get('#ca-edit > a').click()
            cy.get('.mbox-text > span').should("have.text", "Bem-vindo/a! Por decisão da comunidade, é necessário estar regist(r)ado/a para editar ou criar artigos na Wikipédia lusófona.")
        })
        
        it("teste de titulo com falha(negativo)", () => {
            cy.visit("https://www.wikipedia.org/")
            cy.get("#searchInput").type('"titulo inexistente 123"')
            cy.get('.pure-button').click()
            cy.get('.mw-search-nonefound').should("have.text", "\nA pesquisa não produziu resultados.")
        })

        it("teste de login com falha (negativo)", () => {
            cy.visit("https://www.wikipedia.org/");
            cy.get('#js-link-box-pt').click();
            cy.get('#pt-login-2 > a > span').click();
            cy.get('#wpName1').type("nome_incorreto");
            cy.get('#wpPassword1').type("senha_incorreta");
            cy.get('#wpLoginAttempt').click();
        
            cy.get('.cdx-message__content').then(($mensagem) => {
                const texto = $mensagem.text();
        
                if (
                    texto.includes("Existem problemas com alguns dos dados introduzidos.") ||
                    texto.includes("O nome de utilizador ou a palavra-passe inseridos estão incorretos.\nTente novamente, por favor.")
                ) {
                    expect(texto).to.exist;
                } else {
                    throw new Error("Mensagem de erro inesperada: " + texto);
                }
            });
        });
    })