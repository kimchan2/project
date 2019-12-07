<?php

if($_GET[select_type] != "") {
	setcookie("selectType", "{$_GET[select_type]}", time()+86400*30,"/");
	$_COOKIE["selectType"] = $_GET[select_type]; //for cookie save
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
	display: none;
	flex-grow: 2;
	height: 100%;
}

.table-container {
	margin: auto; !important;
	width: 100%
}

.content-table {
	width: 100%;
}

.th-ele {
	text-align: left;
}

#select-form, #form {
	display: inline-block;
}

#bt {
	width: 60px;
	height: 35px;
	border: 0px;
	background: #1b5ac2;
	outline: none;
	float: right;
	color: #ffffff;
	cursor: pointer;
	font-size: 15px;
	font-weight: bold;
}

#select-type {
	font-size: 13px;
	width: 150px;
	height: 35px;
	border: 5px ridge #1b5ac2;
	float: left;
	cursor: pointer;
}

</style>

<!--date script-->
<script src="//code.jquery.com/jquery-3.3.1.min.js"></script>
<script type="text/javascript">

//today
var today = new Date();
var day = today.getDate();
var month = today.getMonth()+1;
var year = today.getFullYear();

if (day < 10) {
	day = '0'+day;
}

if (month < 10) {
	month = '0'+month;
}

//6month ago
var lastDay = new Date();
var last = lastDay.getTime()-(180*24*60*60*1000);
lastDay.setTime(last);
var lastYear = lastDay.getFullYear();
var lastMonth = lastDay.getMonth()+1;
var lastDate = lastDay.getDate();

if (lastDate < 10) {
	lastDate = '0'+lastDate;
}

if (lastMonth < 10) {
	lastMonth = '0'+lastMonth;
}

$(document).ready(function() {
	document.getElementById("from_date").value = lastYear+'-'+lastMonth+'-'+lastDate;
	document.getElementById("to_date").value = year+'-'+month+'-'+day;

	//right-content script
	if("<?= $_GET[select_type] ?>" != "") {
		var board = document.getElementsByClassName('right-content');
		board[0].style.display = "block";
	}
});

</script>

</head>
<body>
	<div class="container">
		<div><a class="title-text" id="title-big" href="ig.php" style="text-decoration:none">IG</a><a class="title-text" id="title-small" href="ig.php" style="text-decoration:none">industry_gate</a>
		</div>
	</div>
	<div class="content">
		<div class="box-container">
			<div class="table-container">
				<form action="./ig.php" method="get" id="container-form">
					<table cellpadding=0 cellspacing=0 width=100%>	
						<tr>
							<td style="text-align: center;">
								<div id="date-select">
									<input type="date" value="2019-02-10" id="from_date" name="from_date">
									<input type="date" value="2019-12-10" id="to_date" name="to_date">
								</div>
							</td>
							<td style="text-align: center;">
								<div id="select-form">
									<select name="select_type" id="select-type">
										<option value="" style="font-weight: bold;">선택하세요</option>
										<option class="selectclass" id="5G" value="5G" <?php if($_COOKIE[selectType] == "5G"){echo "selected"; }?> > 5G </option>
										<option class="selectclass" id="cloud" value="클라우드" <?php if($_COOKIE[selectType] == "클라우드"){echo "selected"; }?>> 클라우드</option>
										<option class="selectclass" id="AI" value="인공지능" <?php if($_COOKIE[selectType] == "인공지능"){echo "selected"; }?>> 인공지능</option>
										<option class="selectclass" id="blockchain" value="블록체인" <?php if($_COOKIE[selectType] == "블록체인"){echo "selected"; }?>> 블록체인</option>
										<option class="selectclass" id="smartfactory" value="스마트팩토리" <?php if($_COOKIE[selectType] == "스마트팩토리"){echo "selected"; }?>> 스마트팩토리</option>
									</select>
									<div id="form">
										<input type="submit" value="search" id="bt">
									</div>
								</div>
							</td>
						</tr>
					</table>
				</form>
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
