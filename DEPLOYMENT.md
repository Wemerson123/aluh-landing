# ALUH Jewels — publicação e operação

GitHub Pages publica `main` na raiz `/` (legacy). CNAME: `www.aluhjewels.com`. Landing e catálogo visual ficam no GitHub; produtos, carrinho, newsletter e checkout usam `shop.aluhjewels.com`. Imagens usam CDN Shopify direto. Visual e animações preservados.

## Catálogo

Snapshot estático de 170 itens em shop.html: preços, estoque, imagens e descrições não sincronizam. Shopify é a fonte final; atualizar snapshot ou sincronizar futuramente. Nenhum produto/preço foi alterado. 168 handles constam no products.json público; eternity-baguette-band e fleur-d-or-necklace abriram em páginas individuais com Add to cart em 23/10/2026, portanto foram preservados.

## DNS pendente — observado em 23/10/2026

- @ A: manter 185.199.108.153; adicionar 185.199.109.153, 185.199.110.153, 185.199.111.153.
- @ AAAA: remover 2620:127:f00f:a:: (Shopify). Opcionalmente substituir pelos quatro IPv6 GitHub: 2606:50c0:8000::153, 2606:50c0:8001::153, 2606:50c0:8002::153, 2606:50c0:8003::153.
- www CNAME: trocar shops.myshopify.com por wemerson123.github.io.
- shop CNAME: preservar shops.myshopify.com.
- Preservar nameservers, MX, TXT e e-mail; não resetar DNS.
- Confirmar shop.aluhjewels.com como domínio principal Shopify. Produtos/checkout não devem redirecionar para www.
- Menu Home/logo da Shopify retorna à própria loja. Adicionar link para https://www.aluhjewels.com no menu após domínio ativo.

Referência oficial: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site

## SEO após domínio/HTTPS

Canonical, Open Graph, Twitter e sitemap preparados. noindex, follow e robots Disallow mantidos durante migração, enquanto www ainda serve Shopify. Depois do DNS/certificado, confirmar Settings > Pages > Enforce HTTPS. Executar `python3 scripts/activate-seo.py` com rede: valida HTTPS/conteúdo das duas páginas, redirect apex e antiga URL github.io; só então libera metas e robots. Revisar diff, commit, push e revalidar publicado. Qualquer falha mantém arquivos intactos.

Search Console/Analytics não configurados. Newsletter usa POST nativo Shopify /contact (form_type=customer, contact[email], contact[tags]=newsletter), sem simular sucesso. Validar entrega com email autorizado; nenhum cadastro real enviado.

## Testes e dependências

Browser Harness/CDP, desktop 1200 e mobile 390. Nenhuma compra real. React 18, Framer Motion, Babel e Tailwind CDN mantidos; avisos de compilação/CDN em produção são limitações existentes. Navegação fallback funciona sem dependências. Sem bibliotecas novas. Consulte o relatório entregue para resultados e limites.
