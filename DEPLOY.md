# Recomendações de Deploy & Cache — Tropical Pet Shop

Este documento descreve as diretrizes arquiteturais recomendadas para publicação do site em qualquer provedor de hospedagem (Nginx, Apache, Caddy, Vercel, Netlify, Cloudflare Pages, AWS S3/CloudFront), sem atrelamento a plataformas específicas.

---

## 1. Políticas de Cache-Control por Tipo de Recurso

Para maximizar a retenção em cache dos navegadores e eliminar latência de rede em visitas repetidas:

### A. Ativos Estáticos Imutáveis (`/site/fonts/*`, `/site/assets/*`, `/site/js/vendor/*`)
Arquivos binários que não mudam frequentemente:
```http
Cache-Control: public, max-age=31536000, immutable
```
- **Validade:** 1 ano (31.536.000 segundos).
- **Justificativa:** Fontes WOFF2 locais e imagens WebP compactadas devem ser cacheadas permanentemente pelo cliente.

### B. Folhas de Estilo e Scripts (`/site/css/*.css`, `/site/js/*.js`)
Recursos de código sujeitos a melhorias contínuas:
```http
Cache-Control: public, max-age=604800, stale-while-revalidate=86400
```
- **Validade:** 7 dias, com tolerância de 24 horas para servir versão em cache enquanto revalida em segundo plano (*stale-while-revalidate*).

### C. Documento HTML Principal (`/index.html`)
Ponto de entrada do site:
```http
Cache-Control: public, max-age=0, must-revalidate
```
- **Justificativa:** Garante que qualquer atualização no site seja imediatamente detectada pelo visitante sem necessidade de limpeza manual de cache (*hard refresh*).

---

## 2. Compressão de Rede (Brotli & Gzip)

O servidor deve estar configurado para servir compressão **Brotli (`br`)** com fallback para **Gzip (`gzip`)** em todos os tipos de conteúdo baseados em texto:
- `text/html`
- `text/css`
- `application/javascript`
- `image/svg+xml`
- `application/json`

---

## 3. Cabeçalhos de Segurança Recomendados (Security Headers)

```http
# Prevenção de MIME Sniffing
X-Content-Type-Options: nosniff

# Proteção contra Clickjacking
X-Frame-Options: SAMEORIGIN

# Controle de Referenciador
Referrer-Policy: strict-origin-when-cross-origin

# Restrição de APIs Nativas de Dispositivo
Permissions-Policy: camera=(), microphone=(), geolocation=()

# Política de Segurança de Conteúdo (CSP estrita para site estático auto-hospedado)
Content-Security-Policy: default-src 'self' 'unsafe-inline'; font-src 'self' data:; img-src 'self' data:; connect-src 'self'; script-src 'self' 'unsafe-inline';
```

---

## 4. Exemplos de Configuração por Servidor

### Exemplo Nginx (`nginx.conf` ou bloco de site)
```nginx
location ~* \.(woff2|webp|png|jpg|jpeg|gif|ico)$ {
    expires 1y;
    add_header Cache-Control "public, max-age=31536000, immutable";
    access_log off;
}

location ~* \.(css|js)$ {
    expires 7d;
    add_header Cache-Control "public, max-age=604800, stale-while-revalidate=86400";
}

location = /index.html {
    add_header Cache-Control "public, max-age=0, must-revalidate";
}
```

### Exemplo Apache (`.htaccess`)
```apache
<IfModule mod_expires.c>
    ExpiresActive On
    ExpiresByType font/woff2 "access plus 1 year"
    ExpiresByType image/webp "access plus 1 year"
    ExpiresByType text/css "access plus 1 week"
    ExpiresByType application/javascript "access plus 1 week"
    ExpiresByType text/html "access plus 0 seconds"
</IfModule>
```
