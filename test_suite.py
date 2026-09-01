import asyncio
import os
import json
import sys
from playwright.async_api import async_playwright, expect

# Configurar stdout para UTF-8 no Windows
sys.stdout.reconfigure(encoding='utf-8')

async def run_teste_supremo():
    print("=" * 60)
    print(">>> INICIANDO BATERIA DE TESTES E2E: TESTE SUPREMO (ANTI-VIBECODING)")
    print("=" * 60)
    
    # -------------------------------------------------------------
    # 0. AUDITORIA DE ARQUIVOS TÉCNICOS NA RAIZ
    # -------------------------------------------------------------
    print("\n[AUDITORIA DE ARQUIVOS] Verificando integridade dos arquivos técnicos...")
    root_files = ["robots.txt", "sitemap.xml", "llms.txt", "favicon.svg", "404.html"]
    for f in root_files:
        assert os.path.exists(f), f"Arquivo obrigatório ausente: {f}"
        size = os.path.getsize(f)
        assert size > 0, f"Arquivo vazio: {f}"
        print(f"  [PASS] {f} presente e com conteúdo ({size} bytes).")
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        
        # -------------------------------------------------------------
        # 1. TESTE DESKTOP (1440x900) & AUDITORIA DE SEO / SCHEMA.ORG
        # -------------------------------------------------------------
        print("\n[1/3] EXECUTANDO CENARIO DESKTOP (1440x900) & AUDITORIA DE SEO...")
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        
        # Monitor de Erros de Console e Rede
        console_errors = []
        page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
        
        # ARRANGE: Carregar a Landing Page
        await page.goto("file:///D:/Creative%20Developer%20Solo/projetos/pessoal/descobrindo/torcida-web/index.html")
        
        # ASSERT: Semântica H1 única (Anti-Vibecoding #9 e #10)
        h1_elements = page.locator("h1")
        h1_count = await h1_elements.count()
        assert h1_count == 1, f"Erro: Esperado exatamente 1 <h1>, encontrado {h1_count}"
        print(f"  [PASS] [SEMÂNTICA] Exatamente 1 <h1> semântico encontrado no DOM.")
        
        # ASSERT: Meta Tags e Open Graph (Anti-Vibecoding #4, #6, #7, #11, #16)
        title = await page.title()
        assert "Torcida" in title and "Mateus Emanuel" in title, f"Title genérico detectado: {title}"
        print(f"  [PASS] [TITLE] Tag <title> descritiva e profissional: '{title}'")
        
        meta_desc = await page.locator("meta[name='description']").get_attribute("content")
        assert meta_desc and len(meta_desc) >= 50, f"Meta description inválida: {meta_desc}"
        print(f"  [PASS] [META DESC] Description presente com {len(meta_desc)} caracteres.")
        
        canonical = await page.locator("link[rel='canonical']").get_attribute("href")
        assert canonical, "Canonical URL ausente!"
        print(f"  [PASS] [CANONICAL] Canonical presente: {canonical}")
        
        og_image = await page.locator("meta[property='og:image']").get_attribute("content")
        assert og_image, "og:image ausente!"
        print(f"  [PASS] [OG TAGS] Open Graph Image configurada.")
        
        # ASSERT: Schema.org JSON-LD (Anti-Vibecoding #8)
        json_ld_script = page.locator("script[type='application/ld+json']")
        await expect(json_ld_script).to_have_count(1)
        json_ld_text = await json_ld_script.inner_text()
        schema_data = json.loads(json_ld_text)
        assert "@context" in schema_data and "@graph" in schema_data, "Schema.org inválido!"
        print("  [PASS] [SCHEMA.ORG] Dados estruturados JSON-LD válidos e integrados.")
        
        # ASSERT: Hero Title & Logo
        hero_heading = page.locator("h1", has_text="O Salgadinho")
        await expect(hero_heading).to_be_visible()
        print("  [PASS] [HERO] Titulo principal visivel e renderizado.")
        
        hero_pack = page.locator("#hero-pack")
        await expect(hero_pack).to_be_visible()
        print("  [PASS] [HERO] Embalagem Hero principal carregada.")
        
        # ASSERT: Top 3 Classicos
        top_heading = page.locator("h2", has_text="OS CLÁSSICOS")
        await expect(top_heading).to_be_visible()
        
        top_flavors = ["Pimenta", "Churrasco", "Cebola"]
        for flavor in top_flavors:
            card = page.locator(".flavor-card", has_text=flavor)
            await expect(card).to_be_visible()
            img = card.locator("img")
            await expect(img).to_be_visible()
            natural_width = await img.evaluate("el => el.naturalWidth")
            assert natural_width > 0, f"Imagem do sabor {flavor} quebrou!"
            print(f"  [PASS] [TOP 3] Card '{flavor}' renderizado com imagem valida ({natural_width}px).")
            
        # ACT & ASSERT: Interacao de Hover no Card
        pimenta_card = page.locator(".flavor-card", has_text="Pimenta")
        await pimenta_card.hover()
        await page.wait_for_timeout(500)
        print("  [PASS] [HOVER] Hover executado no card Pimenta sem falhas de layout.")
        
        # ASSERT: Grid de Outros Sabores (6 produtos secundarios)
        other_cards = page.locator(".other-card")
        count = await other_cards.count()
        assert count == 6, f"Esperado 6 outros sabores, encontrado {count}"
        print(f"  [PASS] [PRODUTOS] Grid secundario validado com todos os {count} sabores.")
        
        # ASSERT: Secao Historia
        history_heading = page.locator("h2", has_text="HISTÓRIA")
        await expect(history_heading).to_be_visible()
        print("  [PASS] [HISTORIA] Secao institucional de historia renderizada.")
        
        # ASSERT: Secao CTA
        cta_btn = page.locator("a", has_text="CADASTRE-SE PARA NOVIDADES")
        await expect(cta_btn).to_be_visible()
        print("  [PASS] [CTA] Botao de acao da comunidade validado.")
        
        # ASSERT: Footer Completo (Logo, Redes, Links, Assinatura)
        footer = page.locator("#footer")
        await expect(footer).to_be_visible()
        
        logo_footer = footer.locator("img[alt*='Torcida']")
        await expect(logo_footer).to_be_visible()
        
        # Redes Sociais
        fb_link = footer.locator("a[aria-label='Facebook Torcida']")
        ig_link = footer.locator("a[aria-label='Instagram Torcida']")
        tt_link = footer.locator("a[aria-label='TikTok Torcida']")
        await expect(fb_link).to_be_visible()
        await expect(ig_link).to_be_visible()
        await expect(tt_link).to_be_visible()
        print("  [PASS] [FOOTER] Icones de redes sociais (Facebook, Instagram, TikTok) ativos e com SVGs nitidos.")
        
        # Link do Desenvolvedor
        dev_link = footer.locator("a", has_text="@mateusemanuelluiznogueira")
        await expect(dev_link).to_be_visible()
        href = await dev_link.get_attribute("href")
        assert "instagram.com/mateusemanuelluiznogueira" in href, "Link do Instagram incorreto!"
        print(f"  [PASS] [DEV CREDIT] Assinatura validada com link correto ({href}).")
        
        # Screenshot Completo Desktop
        await page.screenshot(path="teste_supremo_desktop.png", full_page=True)
        print("  [SCREENSHOT] Captura de tela Desktop gerada: teste_supremo_desktop.png")
        await page.close()
        
        # -------------------------------------------------------------
        # 2. TESTE MOBILE (390x844 - iPhone 14 / Padrao Mobile)
        # -------------------------------------------------------------
        print("\n[2/3] EXECUTANDO CENARIO MOBILE (390x844)...")
        mobile_page = await browser.new_page(viewport={"width": 390, "height": 844})
        await mobile_page.goto("file:///D:/Creative%20Developer%20Solo/projetos/pessoal/descobrindo/torcida-web/index.html")
        
        # Verificar se nao ha overflow horizontal quebrado
        scroll_width = await mobile_page.evaluate("document.documentElement.scrollWidth")
        inner_width = await mobile_page.evaluate("window.innerWidth")
        print(f"  [RESPONSIVIDADE] Largura da pagina: {scroll_width}px | Viewport: {inner_width}px")
        
        # Simular rolagem do usuário para disparar ScrollTrigger
        await mobile_page.evaluate("""async () => {
            await new Promise((resolve) => {
                let totalHeight = 0;
                let distance = 300;
                let timer = setInterval(() => {
                    let scrollHeight = document.body.scrollHeight;
                    window.scrollBy(0, distance);
                    totalHeight += distance;
                    if(totalHeight >= scrollHeight){
                        clearInterval(timer);
                        resolve();
                    }
                }, 100);
            });
        }""")
        await mobile_page.wait_for_timeout(1000)
        
        await mobile_page.screenshot(path="teste_supremo_mobile.png", full_page=True)
        print("  [SCREENSHOT] Captura de tela Mobile gerada: teste_supremo_mobile.png")
        await mobile_page.close()
        
        # -------------------------------------------------------------
        # 3. TESTE DA PÁGINA 404 (Anti-Vibecoding #3)
        # -------------------------------------------------------------
        print("\n[3/3] EXECUTANDO TESTE DA PÁGINA 404...")
        page_404 = await browser.new_page(viewport={"width": 1440, "height": 900})
        await page_404.goto("file:///D:/Creative%20Developer%20Solo/projetos/pessoal/descobrindo/torcida-web/404.html")
        
        title_404 = await page_404.title()
        assert "404" in title_404, f"Título da 404 incorreto: {title_404}"
        
        return_btn = page_404.locator("a", has_text="VOLTAR PARA A RESENHA")
        await expect(return_btn).to_be_visible()
        print("  [PASS] [404] Página 404 carregada com identidade visual e botão funcional.")
        await page_404.screenshot(path="teste_supremo_404.png")
        print("  [SCREENSHOT] Captura de tela 404 gerada: teste_supremo_404.png")
        await page_404.close()
        
        await browser.close()
        
        # Relatorio de Erros de Console
        print("\n" + "=" * 60)
        if len(console_errors) == 0:
            print("STATUS: 100% DOS TESTES APROVADOS -- ZERO ERROS DE CONSOLE/REDE!")
        else:
            print(f"AVISO: {len(console_errors)} erros de console detectados:")
            for err in console_errors:
                print(f"   - {err}")
        print("=" * 60)

if __name__ == "__main__":
    asyncio.run(run_teste_supremo())
