# Sitemap Generator
This project is not meant for automatically crawling a website and obtaining all its endpoints. This web is for those who already have a list of endpoints, or those who have few endpoints and could manually input them. 
## Example
This
```
http://127.0.0.1:5000/
```
and this
```
1
2
3
4
```
generates this
```
<?xml version="1.0" ?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
   <url>
      <loc>http://127.0.0.1:5000/</loc>
      <lastmod>2019-10-30</lastmod>
   </url>
   <url>
      <loc>http://127.0.0.1:5000/1</loc>
      <lastmod>2019-10-30</lastmod>
   </url>
   <url>
      <loc>http://127.0.0.1:5000/2</loc>
      <lastmod>2019-10-30</lastmod>
   </url>
   <url>
      <loc>http://127.0.0.1:5000/3</loc>
      <lastmod>2019-10-30</lastmod>
   </url>
   <url>
      <loc>http://127.0.0.1:5000/4</loc>
      <lastmod>2019-10-30</lastmod>
   </url>
</urlset>
```
