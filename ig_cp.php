<?php

if($_GET[select_type] != "") {
	setcookie("selectType", "{$_GET[select_type]}", time()+86400*30,"/");
	$_COOKIE["selectType"] = $_GET[select_type];
}

?>
<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta http-equiv="X-UA-Compatible" content="IE=edge, chrome=1"/>
<title>Industry Gate</title>

<style>
html {
	height: 100%;
}

body {
	height: 90%;
	margin: 0;
	background-color: #E0FFFF;
}

.title-text {
	font-family: "Gill Sans", sans-serif;
	text-align: center;
	margin: auto; !important;
	margin-bottom: 10px;
	padding: 5px;
	width: 100%;
}

#title-big {
	font-size: 50px;
	color: #2F4F4F;
	font-weight: 700;
}

#title-small {
	color: #556B2F;
}

.container {
	margin: auto; !important;
	margin-top: 10px;
	height: 40px;
	width: 300px;
	text-align: center;
}

.content {
	height: 100%;
	margin-top: 20px;
}

.footer {
	display: block;
	text-align: right;
	width: 100%;
	padding-bottom: 10px;
}

#date-select {
	margin: auto;
}

.box-container {
	margin: auto; !important;
	width: 700px;
	padding-top: 20px;
}

.content-container {
	margin: auto; !important;
	padding-top: 25px;
	display: flex;
	height: 80%;
}

.left-content {
	flex-grow: 1;
	height: 100%;
}

.right-content {
	flex-grow: 2;
	height: 100%;
}

.table-container {
	margin: auto; !important;
	width: 100%;
}

#form {
	height: 35px;
	width: 100%;
	border: 2px solid #1b5ac2;
	background: #ffffff;
	display: inline-block;
	float: right;
	padding-top: 1px;
	margin: auto; !important;
	text-align: center;
}

#input {
	font-size: 12px;
	width: calc(100%-70px);
	padding: 10px;
	border: 0px;
	outline: none;
	float: left;
}

#bt {
	width: 50px;
	height: 35px;
	border: 0px;
	background: #1b5ac2;
	outline: none;
	float: right;
	color: #ffffff;
	cursor: pointer;
}

.content-table {
	width: 100%;
}

.th-ele {
	text-align: left;
}

#select-type {
	margin: auto; !important;
	text-align: center;
}

</style>
</head>
<body>
	<div class="container">
		<div><a class="title-text" id="title-big" href="ig.php" style="text-decoration:none">IG</a><a class="title-text" id="title-small" href="ig.php" style="text-decoration:none">industry_gate</a>
		</div>
	</div>
	<div class="content">
		<div class="box-container">
			<div class="table-container">
				<table cellpadding=0 cellspacing=0 width=100%>
					<tr>
						<td style="text-align: center;">
							<div id="date-select">
								<input type="date" value="2019-02-10" id="from_date" name="from_date">
								<input type="date" value="2019-12-10" id="to_date" name="to_date">
							</div>
						</td>
						<td style="text-align: center;">
							<div id="form">
								<select name="select_type" id="select-type">
									<option value="">choose</option>
									<option class="selectclass" id="5G" value="5G" <? if($_COOKIE[selectType] == "5G"){echo "5G"; }?> 5G</option>
									<option class="selectclass" id="cloud" value="cloud" <? if($_COOKIE[selectType] == "cloud"){echo "cloud"; }?> cloud</option>
									<option class="selectclass" id="AI" value="AI" <? if($_COOKIE[selectType] == "AI"){echo "AI"; }?> AI</option>
							</div>
						</td>
					</tr>
				</table>
			</div>
		</div>
		<div class="content-container">
			<div class="left-content">
			</div>
			<div class="right-content">
				<table class="content-table">
					<thead>
					<tr>
						<th class="th-ele">number</th>
						<th class="th-ele">title</th>
						<th class="th-ele">source</th>
						<th class="th-ele">date</th>
					</tr>
					</thead>
					<tbody>
					<tr>
						<td>1</td>
						<td>how...</td>
						<td>ayoung</td>
						<td>2019.12.01</td>
					</tr>
					</tbody>
				</table>
			</div>
		</div>
		<div class="footer">
		</div>
	</div>
</body> 
