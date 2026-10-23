# Verificação ALUH — 23/10/2026, aproximadamente 13h Brisbane

## Publicação e domínio

- GitHub Pages built, main na raiz, CNAME www.aluhjewels.com, HTTPS obrigatório ativo.
- Certificado www aprovado, válido até 21/01/2027; resposta HTTPS 200 validada usando resolução explícita para 185.199.108.153, sem ignorar verificação TLS.
- index.html e shop.html obtidos por HTTPS no domínio oficial são idênticos aos arquivos do commit db78234 (SHA1 049b0534904ef668ce88674d31ba975cf375fcb0 e 5585b3eb52e65c658de6a7c41111f09855bc9010 antes da correção de escape).
- www CNAME correto nos autoritativos b1/b2 e nos resolvedores 1.1.1.1/8.8.8.8. IPv4 e IPv6 de www seguem GitHub via CNAME. Cache local ainda resolve Shopify; navegador local redirecionou www para shop. A consulta externa da homepage já encontrou a landing ALUH.
- @ A 185.199.108.153 preservado; não solicitar outros A devido à limitação do painel confirmada pelo usuário.
- @ AAAA 2620:127:f00f:a:: ainda presente nos autoritativos. Deve ser removido pela cliente/autorização DNS. Não foi alterado.
- HTTP apex por IPv4 retorna 301 para HTTPS www. HTTPS apex falha por certificado sem cobertura para aluhjewels.com, inclusive no IP GitHub. Não declarar redirecionamento HTTPS apex concluído. Corrigir AAAA e reavaliar emissão/cobertura do certificado GitHub após propagação.
- URL antiga github.io já redireciona ao domínio configurado; SEO permanece bloqueado até verificação pública completa.

## Shopify

- Loja pública abre em shop.aluhjewels.com; CNAME shops.myshopify.com preservado.
- Produto Pearl Eclipse Earrings abre, variante 48751866839291 disponível.
- Carrinho inicial vazio. Adicionada uma unidade para teste; cart exibiu produto e total A$79.
- Rota /checkout abriu checkout Shopify seguro no host shop.aluhjewels.com, com produto correto, entrega e opções cartão/PayPal. Nenhum dado pessoal ou pagamento inserido; nenhuma compra realizada.
- Item do teste removido via cart/change.js. Carrinho restaurado e confirmado com item_count=0.
- A listagem pública contém 168 produtos. Os dois handles do snapshot ausentes da listagem continuam com páginas individuais válidas; catálogo estático de 170 preservado.
- Coleções da landing conferidas com collections.json público; links comerciais usam shop. Home/logo da Shopify retornam à própria loja, sem link institucional novo aplicado.

## Código e navegação

- CNAME exato confirmado; todos os caminhos locais de href/src existem; nenhum link antigo www/products ou www/cart.
- Corrigido escape de aspas em títulos usados em atributos do catálogo. Sem mudança de CSS, design ou animações.
- Documentação atualizada para não exigir vários A e distinguir DNS autoritativo de cache.
- Browser Harness/CDP: landing e catálogo locais testados em 390, 768, 1280 e 1920 pixels, sem overflow horizontal. Arquivos equivalentes aos publicados antes da correção de escape; publicação final deve ser revalidada após deploy.
- Sem erros JS capturados nos fluxos testados. Modal abre com produto correto e Buy aponta shop. Filtro Pearls mostra 13 e oculta Show more; paginação passa de 24 para 48.
- Capturas desktop/mobile revisadas; imagens carregaram sem falhas detectadas no catálogo. Dependências CDN e runtime existentes preservados.
- Newsletter não reenviada; entrega real segue sem teste, para evitar inscrição sem consentimento do titular do email.

## SEO e pendências únicas

O script activate-seo.py foi executado com rede e recusou ativação porque o acesso normal a www ainda chega ao conteúdo/destino Shopify. Nenhuma meta nem robots foi liberado. Canonical/OG/sitemap já estão preparados.

1. Cliente remover apenas AAAA @ 2620:127:f00f:a::; preservar shop, MX, TXT e nameservers.
2. Aguardar propagação do www já correto (TTL autoritativo 86400s), revalidar acesso normal e certificado/redirecionamento HTTPS apex. Se continuar sem cobertura apex, acompanhar GitHub Pages/certificado antes de concluir.
3. Após verificações passarem, executar scripts/activate-seo.py, revisar, publicar e verificar robots/metas no domínio oficial.
4. Se desejado concluir retorno institucional da Shopify: adicionar Site ALUH -> https://www.aluhjewels.com no menu com acesso autorizado ao admin. Entrega newsletter exige teste com email consentido. Nenhuma autenticação ou integração Search Console/Analytics foi presumida.
