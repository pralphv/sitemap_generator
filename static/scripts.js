let XML_RESULT = null;
const GITHUB_URL = "https://github.com/pralphv/sitemap_generator"

function handleOnClick() {
  let win = window.open(GITHUB_URL, '_blank');
  win.focus();
}

function setXmlResult(value) {
    XML_RESULT = value;
}

function getXmlResult() {
    return XML_RESULT;
}

function getById(id) {
    const node = document.getElementById(id);
    return node;
}

async function handleOnSubmit(e) {
    const url = getById("url").value;
    let endPoints = getById("endPoints").value;
    let languages = getById("languages").value;
    if (!url || !endPoints) {
        return;
    }
    endPoints = endPoints.split("\n");
    languages = languages? languages.split("\n"): null;

    const resp = await fetch("/api", {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            url: url,
            endPoints: endPoints,
            languages: languages,
            prettify: true
        })
    });
    const obj = await resp.json();
    console.log(obj)
    const xmlResult = obj.xml;
    setXmlResult(xmlResult);
    let quineHtml = prettify(xmlResult);
    document.getElementById("result").innerHTML = quineHtml;
}

function prettify(s) {
    s = s
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;');

    s = s.replace(
        /&lt;script src[\s\S]*?&gt;&lt;\/script&gt;|&lt;!--\?[\s\S]*?--&gt;|&lt;pre\b[\s\S]*?&lt;\/pre&gt;/g,
        '<span class="operative">$&<\/span>'
    );
    return s
}

function prettyPlaceholder() {
    let text = `<?xml version="1.0" ?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
   <url>
      <loc>https://example.com/</loc>
      <lastmod>2019-10-27</lastmod>
   </url>
   <url>
      <loc>https://example.com/about</loc>
      <lastmod>2019-10-27</lastmod>
   </url>
   <url>
      <loc>https://example.com/account</loc>
      <lastmod>2019-10-27</lastmod>
   </url>
   <url>
      <loc>https://example.com/product/1</loc>
      <lastmod>2019-10-27</lastmod>
   </url>
   <url>
      <loc>https://example.com/product/2</loc>
      <lastmod>2019-10-27</lastmod>
   </url>
   <url>
      <loc>https://example.com/cn</loc>
      <lastmod>2019-10-27</lastmod>
   </url>
   <url>
      <loc>https://example.com/cn/about</loc>
      <lastmod>2019-10-27</lastmod>
   </url>
   <url>
      <loc>https://example.com/cn/account</loc>
      <lastmod>2019-10-27</lastmod>
   </url>
   <url>
      <loc>https://example.com/cn/product/1</loc>
      <lastmod>2019-10-27</lastmod>
   </url>
   <url>
      <loc>https://example.com/cn/product/2</loc>
      <lastmod>2019-10-27</lastmod>
   </url>
   <url>
      <loc>https://example.com/jp</loc>
      <lastmod>2019-10-27</lastmod>
   </url>
   <url>
      <loc>https://example.com/jp/about</loc>
      <lastmod>2019-10-27</lastmod>
   </url>
   <url>
      <loc>https://example.com/jp/account</loc>
      <lastmod>2019-10-27</lastmod>
   </url>
   <url>
      <loc>https://example.com/jp/product/1</loc>
      <lastmod>2019-10-27</lastmod>
   </url>
   <url>
      <loc>https://example.com/jp/product/2</loc>
      <lastmod>2019-10-27</lastmod>
   </url>
</urlset>
`
    getById("result").placeholder = text;
}
prettyPlaceholder();