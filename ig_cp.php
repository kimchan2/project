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
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384- Vkoo8x4CGsO3+ Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384- wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>

<script src="https://code.jquery.com/jquery- 3.4.1.slim.min.js"integrity="sha384- J6qa4849blE2+ poT4WnyKhv5vZF5SrPoOiEjwBvKU7imGFAV0wwj1yYfoRSJoZ+ n" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384- Q6E9RHvblyZFJoft+ 2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>

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
	height: 70%;
}

.left-content {
	flex-grow: 1;
	height: 100%;
	width: 40%;
	padding: 40px;
	padding-right: 0; !important;
}

#picture {
	margin: auto;
	text-align: center;
}

#emotion {
	margin: auto;
	text-align: center;
}

.right-content {
	display: none;
	flex-grow: 2;
	width: 60%;
	height: 100%;
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

#text {
	display: inline-block;
	margin-right: 10px;
}

.pager {
	display: inline-block;
}

.emot-content {
	padding: 10px;
	margin: auto; !important;
	margin-top: 20px;
	font-size: 18px;
	font-weight: bold;
	display: inline-block;
	border: 2px ridge #1b5ac2;
}

#a-<?php if($_GET[page]){echo $_GET[page];}else{echo "0";}?> {
	color: #1b5ac2;
	font-weight: bold;
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
									<section id="text">기간 입력</section>
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
										<option class="selectclass" id="AI" value="AI" <?php if($_COOKIE[selectType] == "AI"){echo "selected"; }?>> 인공지능</option>
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
				<div id="picture">
					<image src="<?=$_GET[select_type]?>.png" onerror="this.style.display='none'" width="500px" height="400px">
				</div>
				<div id="emotion">
				<?php
				$conn = mysqli_connect('localhost','user_name','userpassword','crawling');
				$var = $_GET[select_type];
				if($_GET[select_type] != "") {
					if($_GET[select_type] == "클라우드") {$var="cloud";}
					else if($_GET[select_type] == "블록체인") {$var="BlockChain";}
					else if($_GET[select_type] == "스마트팩토리") {$var="SmartFactory";}
				
				$sql = "SELECT score FROM $var WHERE score is NOT NULL";
				$result = mysqli_query($conn,$sql);
				$size = mysqli_num_rows($result);

				$sum = 0;
				while($row=mysqli_fetch_assoc($result)) {
					$sum += $row['score'];
				}

				$avg = $sum/$size;
				if($avg < -0.25) {echo "<p class='emot-content'>부정적 : ".$avg."</p>";}
				else if($avg > 0.25){echo "<p class='emot-content'>긍정적 : ".$avg."</p>";}
				else {echo "<p class='emot-content'>중립적 : ".$avg."</p>";}
				}
				?>
				</div>
			</div>
			<div class="right-content">
				<table class="table table-striped">
					<thead>
					<tr>
						<th style="width:5%;" class="th-ele">number</th>
						<th style="width:25%;" class="th-ele">title</th>
						<th style="width:15%;" class="th-ele">source</th>
						<th style="width:10%;" class="th-ele">date</th>
					</tr>
					</thead>
					<tbody>
					<?php
					$industry = $_GET[select_type];
					if($industry != "") {
						
						$sql="SELECT * FROM Report WHERE industry = \"'$industry'\"";
						$result = mysqli_query($conn,$sql);
						$total_len = mysqli_num_rows($result);
						$start = 1;

						if(isset($_GET[page])&&($_GET[page])!=0) {
							$start = 1+$_GET[page]*10;
							$sql="select * from Report WHERE industry = \"'$industry'\" ORDER BY id ASC LIMIT $start, 10";
						}else {
							$sql="select * from Report WHERE industry = \"'$industry'\" ORDER BY id ASC LIMIT 10";
						}
						$result=mysqli_query($conn,$sql);

						while($row=mysqli_fetch_assoc($result)) {
							$title=$row['title'];
							if(strlen($title)>40) {
							$title=str_replace($row['title'],mb_substr($row['title'],0,30,"utf-8")."...",$row['title']);
							}
							$day=$row['date'];
							$date=substr($day,1,11);
							$date.=substr($day,24,5);

					?>
					<tr>
						<td><?php echo $start ?></td>
						<td><a href=<?php echo $row['URL']?> target="_blank"><?php echo $title;?></a></td>
						<td><?php echo $row['writer']; ?></td>
						<td><?php echo $date; ?></td>
					</tr><?php ++$start;}?>
					</tbody>
					<?php
					$count = (int)($total_len / 10);
					if($total_len % 10) {$count++;}

					echo "<tr>";
					echo "<td colspan=4 align=center>";

					for($i = 0; $i < $count; $i++) {
						$j=$i+1;
						echo "<a id='a-{$i}' href=./ig.php?from_date=$_GET[from_date]&to_date=$_GET[to_date]&select_type=$_GET[select_type]&page={$i}> [";
						echo $j;
						echo "] </a>";
					}
					}?>
				</table>
			</div>
		</div>
		<div class="footer">
		</div>
	</div>
</body>
</html> 
