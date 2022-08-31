var db = require('./db');
var template = require('./template');
var url = require('url');
var qs = require('querystring');
var sanitizeHtml = require('sanitize-html');

exports.home = function (request, response) {
	db.query(`SELECT * FROM topic`, function (error, topics) {
		db.query(`SELECT * FROM author`, function (error, authors) {
			var title = 'Authors';
			var list = template.list(topics);
			var html = template.HTML(
				title,
				list,
				`
				${template.authorTable(authors)}
				<style>
					table{
						border-collapse: collapse;
					}
					td{
						border:1px solid black;
					}
				</style>
				`
				,
				`<a href="/author/create">Create author</a>`
			);
			response.writeHead(200);
			response.end(html);
		});
	});
};

exports.create = function (request, response) {
	db.query('SELECT * FROM topic', function (error1, topics){
		var title = 'Create author';
		var list = template.list(topics);
		var html = template.HTML(
			title,
			list,
			`
			<form action="/author/create_process" method="post">
				<p>	
					<input type="text" name="name" placeholer="name">
				</p>
				<p>
					<textarea name="profile" placeholder="profile"></textarea>
				</p>
				<p>
					<input type="submit">
				</p>
			</form>
			`,
			`<a href=/author_create>Create author</a>`
		);
		response.writeHead(200);
		response.end(html);
	});
}

exports.create_process = function (request, response) {
	var body = '';
	request.on('data', function(data){
		body += data;
	});
	request.on('end', function() {
		var post = qs.parse(body);
		db.query(
			`INSERT INTO author (name, profile) VALUES (?, ?)`,
			[post.name, post.profile],
			function(error, result) {
				if (error) {
					throw error;
				}
				response.writeHead(302, {Location: `/author`});
				response.end();
			}
		);
	});
};

exports.update = function (request, response) {
	var _url = request.url;
	var queryData = url.parse(_url, true).query;
	db.query(`SELECT * FROM topic`, function (error1, topics) {
		db.query(`SELECT * FROM author`, function (error2, authors) {
			db.query('SELECT * FROM author WHERE id=?', [queryData.id], function (error3, author) {
				var title = 'Authors';
				var list = template.list(topics);
				var html = template.HTML(
					title,
					list,
					template.authorTable(authors) +
					`
					<form action="/author/update_process" method="post">
						<input type="hidden" name="id" value="${author[0].id}">
						<p>
							<input type="text" name="name" value="${sanitizeHtml(author[0].name)}">
						</p>
						<p>
							<textarea name="profile">${sanitizeHtml(author[0].profile)}</textarea>
						</p>
						<p>
							<input type="submit">
						</p>
					<form>
					`
					,
					`<a href="/create">Create author</a>`
				);
				response.writeHead(200);
				response.end(html);
			});
		});
	});
};

exports.update_process = function (request, response) {
	var body = '';
	request.on('data', function (data) {
		body = body + data;
	});
	request.on('end', function () {
		var post = qs.parse(body);
		db.query(
			'UPDATE author SET name=?, profile=? WHERE id=?',
			[post.name, post.profile, post.id],
			function (error, result) {
				response.writeHead(301, { Location: '/author' });
				response.end();
			}
		);
	});
};

exports.delete_process = function (request, response) {
	var body = '';
	request.on('data', function(data) {
		body += data;
	});
	request.on('end', function() {
		var post = qs.parse(body);
		db.query(`DELETE FROM author WHERE id=?`, [post.id], function(error, result) {
			if(error){
				throw error;
			}
			response.writeHead(302, {Location:'/author'});
			response.end();
		});
	});
};