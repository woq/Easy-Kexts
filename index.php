<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Easy-Kexts</title>
    <link rel="stylesheet" href="https://cdn.bootcdn.net/ajax/libs/bulma/0.9.0/css/bulma.min.css">
</head>
<body>
<section class="section" name="Core">
    <div class="container">
        <div class="columns is-vcentered is-centered">
            <table class="table is-bordered ">
                <thead>
                <tr>
                    <th><abbr>类别</abbr></th>
                    <th><abbr>项目名</abbr></th>
                    <th><abbr>版本号</abbr></th>
                    <th><abbr>更新时间</abbr></th>
                    <th><abbr>项目说明</abbr></th>
                    <th><abbr>下载连接</abbr></th>
                </tr>
                </thead>
                <tfoot>
                <tr>
                    <th><span class="tag is-primary is-light">Core</span></th>
                    <th><a href="https://github.com/acidanthera/Lilu" target="_blank"><span class="tag is-primary">acidanthera/Lilu</span></a></th>
                    <th><span class="tag is-info">1.4.5</span></th>
                    <th><span class="tag is-success">2020-07-16</span></th>
                    <th><span class="tag is-warning is-light">说明</span></th>
                    <th><a href="" target="_blank"><span class="tag is-link">Primary</span></a></th>
                </tr>
                <tr>
                    <th><span class="tag is-primary is-light">Core</span></th>
                    <th><a href="https://github.com/acidanthera/Lilu" target="_blank"><span class="tag is-primary">acidanthera/Lilu</span></a></th>
                    <th><span class="tag is-info">1.4.5</span></th>
                    <th><span class="tag is-success">published_at_2020-07-16 browser_download_url</span></th>
                    <th><span class="tag is-warning is-light">说明</span></th>
                    <th><a href="" target="_blank"><span class="tag is-link">Primary</span></a></th>
                </tr>
                </tfoot>
            </table>
        </div>
    </div>
</section>
</body>
</html>
<?php
$context = stream_context_create(
    array(
        "http" => array(
            "header" => "User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
        )
    )
);
$json = json_decode(file_get_contents('https://api.github.com/repos/acidanthera/Lilu/releases/latest',false,$context));
echo $json->tag_name;
?>