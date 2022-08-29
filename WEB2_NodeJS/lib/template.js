module.exports = {
    HTML:function (title, list, control, body) {
        return `
        <!doctype html>
        <html>
        <head>
            <title>WEB1 - ${title}</title>
            <meta charset="utf-8">
        </head>
    
        <body>
            <h1><a href="/">WEB</a></h1>
            ${list}
            ${control}
            ${body}
        </body>
        </html>
        `
    },
    List:function (filelist) {
        var list = '<ol>'
        for (i = 0; i < filelist.length; i++) {
            list = list + `<li><a href="/?id=${filelist[i]}">${filelist[i]}</a></li>`;
        }
        list += '</ol>'
        return list;
    }
}

