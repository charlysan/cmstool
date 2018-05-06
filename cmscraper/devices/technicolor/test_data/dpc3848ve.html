<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
		<META http-equiv="Pragma" CONTENT="no-cache">
		<META HTTP-EQUIV="Cache-Control" CONTENT="no-cache">
		<LINK REL="stylesheet" TYPE="text/css" id="webframe" HREF="cmn/css/webframe.css">
		<script src="./cmn/js/utilityFunctions.js"></script>
		<script src="./i18n/i18nReader.php?lang=en"></script>
		
		<script src="./cmn/js/lib/jquery-1.9.1.js"></script>
		<script src="./cmn/js/lib/jquery-migrate-1.2.1.js"></script>
		<script src="./cmn/js/lib/jquery.validate.js"></script>
		<script src="./cmn/js/lib/jquery.alerts.js"></script>
		<script src="./cmn/js/lib/jquery.alerts.progress.js"></script>
		<script src="./cmn/js/lib/jquery.ciscoExt.js"></script>
		<script src="./cmn/js/lib/jquery.virtualDialog.js"></script>

		<!--monitor user's click event to see if user is active-->
		<script>
		$(document).ready(function() {
			var timoutValue = "900";
			var jsInactTimeout = parseInt(timoutValue) * 1000;
			initLabelForI18n();
			//console.log("inactivity setup timer:",document.URL,jsInactTimeout);
			
			// jsInactTimeout = 5000;	// 5 seconds debug
			var h_timer = null;
			$(document).click(function() {
				// do not handle click if no-login for GA
				if ("" == "") {
					return;
				}			
			
				// do not handle click event when count-down show up
				if ($("#count_down").length > 0) {
					return;
				}
				// console.log(h_timer);
				
				clearTimeout(h_timer);
				h_timer = setTimeout(function(){
					var cnt		= 60;
					var h_cntd  = setInterval(function(){
						$("#count_down").text(--cnt);
						// (1)stop counter when less than 0, (2)hide warning when achieved 0, (3)add another alert to block user action if network unreachable
						if (cnt<=0) {
							clearInterval(h_cntd);	
							jAlert("You have been logged out due to inactivity!");
							location.href="logout.php";
						}
					}, 1000);
					// use jAlert instead of alert, or it will not auto log out untill OK pressed!
					jAlert('Press <b>OK</b> to continue session. Otherwise you will be logged out in <span id="count_down" style="font-size: 200%; color: red;">'+cnt+'</span> seconds!'
					, 'You are being logged out due to inactivity!'
					, function(){
						clearInterval(h_cntd);
					});
				}
				, jsInactTimeout);
			}).trigger("click");
			
			
			$.ajaxSetup({
				beforeSend: function (jqXHR,settings) {
					$.ajax({
						url : "actionHandler/checkLogin.php",
						async : false,
						success : function (isLogin) {
						  if (isLogin == "1") {
							jqXHR.abort();
							alert("Please Login First!");
							location.href="index.php";
						  };
						},
						beforeSend : function () {
						}
					});
				}
			});
		});
		</script>
		<style>
			#contentDiv{
				display: none;
				position: absolute;
			}
			#container{
				position: relative;
			}
			#loading_holder{
				background-image: url('cmn/img/progress_bar.gif');
				background-repeat: no-repeat;
				background-position: 50% 0px;
				position: absolute;
				width: 100%;
				height: 9px;
				margin-top: 20px;
			}
		</style>
	</head>

	<body class="BodyStyle">
	    <div id="skip-to-links">
		  <a href="#mainMenuDiv">Skip to main menu</a>
		  <a href="#subMenuDiv">Skip to sub menu</a>
		  <a href="#contentDiv">Skip to content</a>
		</div>
		<div class="BackgroundStyle">
			<img width="100%" src="./cmn/img/pageBackground.jpg" alt="background image" />
		</div>
		
		<div id="container">	<!--this is the main div-->
		<div id="headDiv"><div id="logoDiv"><span><a class="imglink" target="_blank" href="http://www.technicolor.com">
			<img src="cmn/img/technicolor_logo.png" title="Technicolor Logo" alt="Technicolor Logo" width="156px" height="60px"/></a></span></div><div id="modelDiv"><div class="modelContainer"><span>Technicolor DPC3848VE DOCSIS 3.0 Gateway</span><span class="productName">DPC3848VE</span></div></div><div id="menuDiv"><div id="mainMenuDiv"><div class="mainMenuContainer"><div class="mainMenuBg"></div><table><tr><td><a href="Docsis_system.php" tabindex="0" class="link_tab current"><span><script>document.write(vstatus);</script></span></a></td></tr></table></div></div><div id="subMenuDiv"><div class="subMenuContainer"><ul class="layout_list"><li><a href="Docsis_system.php" tabindex="0" class="link_tab current"><span><script>document.write(vcable3);</script></span></a></li></ul></div></div></div></div>		<div id="loading_holder"></div>
		<div id="contentDiv" tabindex="-1">
			


<script>
	setTitle(vt_docsystem);
	var cableStatus = "OPERATIONAL";
	function LanguageChange()
	{   
		var cf = document.forms[0]; 
		var lang = cf.LanguageSelect.value;
		document.cookie = "lang="+lang;
		location.reload();
	}
	
	$(document).ready(function() {
		RefreshScrn(180000);

		var lang = "en";
		$("#LanguageSelect option[value='"+lang+"']").prop("selected",true);

		if ("" == "") {
			$(".login").show();
		}
	});
</script>

<style>
.std input, select {
	margin: 3px;
}
.top-margin {
	
	margin-top: 50px;
}
</style>

<table class="Top">
	<tr>
		<td colspan="2" class="Top1"></td>
		<td colspan="2" class="Top2"></td>
	</tr>
</table>
<form action="check.php" method="post" id="pageForm">
<!-- Data Table -->
<table class="dataTable">
	<tr>
		<td>
			<table class="nav paramTable login" style="display:none;">
				<tr>
					<td class="bwhead">
						<script >dw(vlogin);</script>
					</td>
					<td class="bwhead1">&nbsp;</td>
					<td class="nav1">&nbsp;</td>
				</tr>
				<tr height="3px">
					<td class="Item1"></td>
					<td class="Item2"></td>
					<td></td>
				</tr>
				<tr>
					<td class="Item1"> </td>
					<td class="Item2"> </td>
					<td class="Item3">
						<table class="std" WIDTH="206">
							<tr>
								<td nowrap>
									<label  for="username_login" ><script >dw(vusername);</script></label>
								</td>
								<td nowrap>
									<input type="text" name="username_login" id="username_login" value="" />
								</td>
							</TR>
							<tr>
								<td nowrap>
									<label  for="password_login" ><script >dw(vpasswd);</script></label>
								</td>
								<td nowrap>
									<input type="password" name="password_login" id="password_login" value="" />
								</td>
							</TR>
							<tr>
								<td nowrap width="118">
									<label for="LanguageSelect"><script >dw(v_Language_Selection);</script></label>
								</td>
								<td nowrap>
									<select id="LanguageSelect" name="LanguageSelect" onchange="LanguageChange()">
										<option id='English' value='en'> <script>dw(v_lang_en)</script></option>
										<option id='French' value='fr'>  <script>dw(v_lang_fr)</script></option>
										<option id='Spanish' value='es'> <script>dw(v_lang_es)</script></option>
										<option id='German' value='de'>  <script>dw(v_lang_de)</script></option>
										<option id='Japanese' value='ja'><script>dw(v_lang_ja)</script></option>
									</select>
								</td>
							</TR>					
							<tr>
								<td colspan="2" align="right">
									<script >showSubmit("login", vlogin, "");</script>
								</td>
							</tr>
						</table>
					</td>
				</tr>
				<tr id="i_HR1">
					<td class="Item1">&nbsp;</td>
					<td class="Item2"></td>
					<td><hr class="std"></td>
				</tr>
			</table>			
			<!-- Modem Information Start -->
			<table class="nav paramTable bm_docsisWanAbout">
				<tr>
					<td class="bwhead">
						<script>dw(vt_docsystem);</script>
					</td>
					<td class="bwhead1">&nbsp;</td>
					<td class="nav1">&nbsp;</td>
				</tr>
				<tr height="3px">
					<td class="Item1"></td>
					<td class="Item2"></td>
					<td></td>
				</tr>
				<tr>
					<td class="Item1"> </td>
					<td class="Item2"> </td>
					<td class="Item3">
						<div class="fieldGroup">
							<div class="fieldRow">
								<div class="fieldLabel longLabel">
									<script>dw(vmodel);</script>
								</div>
								<div class="fieldContent stdbold">
									Technicolor DPC3848VE								</div>
							</div>
							<div class="fieldRow">
								<div class="fieldLabel longLabel">
									<script>dw(vvendor);</script>
								</div>
								<div class="fieldContent stdbold">
									Technicolor								</div>
							</div>
							<div class="fieldRow">
								<div class="fieldLabel longLabel">
									<script>dw(vhwrev);</script>
								</div>
								<div class="fieldContent stdbold">
									12.								</div>
							</div>
							<div class="fieldRow">
								<div class="fieldLabel longLabel">
									<script>dw(vserial);</script>
								</div>
								<div class="fieldContent stdbold">
									123456789								</div>
							</div>
							<div class="fieldRow">
								<div class="fieldLabel longLabel">
									<script>dw(vmac1);</script>
								</div>
								<div class="fieldContent stdbold">
									00:00:00:00:00:00								</div>
							</div>
							<div class="fieldRow">
								<div class="fieldLabel longLabel">
									<script>dw(vbootloader);</script>
								</div>
								<div class="fieldContent stdbold">
									3.4.20.6								</div>
							</div>
							<div class="fieldRow">
								<div class="fieldLabel longLabel">
									<script>dw(vfwname);</script>
								</div>
								<div class="fieldContent stdbold">
									dpc3800-v303r204318-171207a.p7b								</div>
							</div>
							<div class="fieldRow">
								<div class="fieldLabel longLabel">
									<script>dw(vfwbldtime);</script>
								</div>
								<div class="fieldContent stdbold">
									12-07-2017  21:44:24								</div>
							</div>
							<div class="fieldRow">
								<div class="fieldLabel longLabel">
									<script>dw(vcmstatus);</script>
								</div>
								<div class="fieldContent stdbold">
									<script>dw(cableStatus == "OPERATIONAL"? vcm_operational:vcm_notSynced)</script>
								</div>
							</div>
	                         <div class="fieldRow">
                                <div class="fieldLabel longLabel">
                                    <script>dw(vt_wnet_colon);</script>
                                </div>
                                <div class="fieldContent stdbold">
                                    <script>dw(venabled)</script>                                </div>
                            </div>
						</div>
						<br/>
					</td>
				</tr>
			</table>
			<!-- Modem Information End -->
			<table class="nav bm_docsisWanAbout">
				<tr id="i_HR1">
					<td class="Item1">&nbsp;</td>
					<td class="Item2"></td>
					<td><hr class="std"></td>
				</tr>
			</table>
			<!-- Docsis Information Start -->
			<table class="nav paramTable bm_docsisWanCmState">
				<tr>
					<td class="bwhead">
						<script>dw(vcm_state);</script>
					</td>
					<td class="bwhead1">&nbsp;</td>
					<td class="nav1">&nbsp;</td>
				</tr>
				<tr height="3px">
					<td class="Item1"></td>
					<td class="Item2"></td>
					<td></td>
				</tr>
				<tr>
					<td class="Item1"> </td>
					<td class="Item2"> </td>
					<td class="Item3">
						<div class="fieldGroup">
							<div class="fieldRow">
								<div class="fieldLabel longLabel">
									<script>dw(vcm_state_ds);</script>
								</div>
								<div class="fieldContent stdbold">
									<script>dw(vcompeleted)</script>								</div>
							</div>
							<div class="fieldRow">
								<div class="fieldLabel longLabel">
									<script>dw(vcm_state_us);</script>
								</div>
								<div class="fieldContent stdbold">
									<script>dw(vcompeleted)</script>								</div>
							</div>
							<div class="fieldRow">
								<div class="fieldLabel longLabel">
									<script>dw(vcm_state_dhcp);</script>
								</div>
								<div class="fieldContent stdbold">
									<script>dw(vcompeleted)</script>								</div>
							</div>
							<div class="fieldRow">
								<div class="fieldLabel longLabel">
									<script>dw(vcm_state_tftp);</script>
								</div>
								<div class="fieldContent stdbold">
									<script>dw(vcompeleted)</script>								</div>
							</div>
							<div class="fieldRow">
								<div class="fieldLabel longLabel">
									<script>dw(vcm_state_reg);</script>
								</div>
								<div class="fieldContent stdbold">
									<script>dw(vcompeleted)</script>								</div>
							</div>
							<div class="fieldRow">
								<div class="fieldLabel longLabel">
									<script>dw(vcm_state_privacy);</script>
								</div>
								<div class="fieldContent stdbold">
									<script>dw(venabled)</script>								</div>
							</div>
						</div>
						<br/>
					</td>
				</tr>
			</table>
			<!-- Docsis Information End -->
			<table class="nav bm_docsisWanCmState">
				<tr id="i_HR2">
					<td class="Item1">&nbsp;</td>
					<td class="Item2"></td>
					<td><hr class="std"></td>
				</tr>
			</table>
			<!-- Downstream Channel Information Start -->
			<table class="nav paramTable bm_docsisWanDSChannel">
				<tr>
					<td class="bwhead">
						<script>dw(vdsch);</script>
					</td>
					<td class="bwhead1">&nbsp;</td>
					<td class="nav1">&nbsp;</td>
				</tr>
				<tr height="3px">
					<td class="Item1"></td>
					<td class="Item2"></td>
					<td></td>
				</tr>
				<tr>
					<td class="Item1"> </td>
					<td class="Item2"> </td>
					<td class="Item3">
						<table class="std" summary="this table shows downstream channel information">
							<thead><tr><th align="left" id="ds_channel" width="140" nowrap><script>dw(vChannel);</script></th><th align="left" id="ds_power" width="140" class="stdbold" nowrap><script>dw(vch_pwr);</script></th><th align="left" id="ds_snr" class="stdbold" nowrap><script>dw(vdsch_snr);</script></th></tr></thead><tbody><tr><td headers="ds_channel" width="140" nowrap><script>dw(vs_channel);</script> 1<script>dw(vcolon);</script></td><td headers="ds_power" nowrap>6.300 <script>dw(vdbmv);</script></td><td headers="ds_snr" nowrap>34.48<script>dw(vdb);</script></td></tr><tr><td headers="ds_channel" width="140" nowrap><script>dw(vs_channel);</script> 2<script>dw(vcolon);</script></td><td headers="ds_power" nowrap>11.000 <script>dw(vdbmv);</script></td><td headers="ds_snr" nowrap>37.35<script>dw(vdb);</script></td></tr><tr><td headers="ds_channel" width="140" nowrap><script>dw(vs_channel);</script> 3<script>dw(vcolon);</script></td><td headers="ds_power" nowrap>10.600 <script>dw(vdbmv);</script></td><td headers="ds_snr" nowrap>37.09<script>dw(vdb);</script></td></tr><tr><td headers="ds_channel" width="140" nowrap><script>dw(vs_channel);</script> 4<script>dw(vcolon);</script></td><td headers="ds_power" nowrap>10.700 <script>dw(vdbmv);</script></td><td headers="ds_snr" nowrap>36.61<script>dw(vdb);</script></td></tr><tr><td headers="ds_channel" width="140" nowrap><script>dw(vs_channel);</script> 5<script>dw(vcolon);</script></td><td headers="ds_power" nowrap>11.400 <script>dw(vdbmv);</script></td><td headers="ds_snr" nowrap>36.61<script>dw(vdb);</script></td></tr><tr><td headers="ds_channel" width="140" nowrap><script>dw(vs_channel);</script> 6<script>dw(vcolon);</script></td><td headers="ds_power" nowrap>11.300 <script>dw(vdbmv);</script></td><td headers="ds_snr" nowrap>36.61<script>dw(vdb);</script></td></tr><tr><td headers="ds_channel" width="140" nowrap><script>dw(vs_channel);</script> 7<script>dw(vcolon);</script></td><td headers="ds_power" nowrap>10.500 <script>dw(vdbmv);</script></td><td headers="ds_snr" nowrap>36.61<script>dw(vdb);</script></td></tr><tr><td headers="ds_channel" width="140" nowrap><script>dw(vs_channel);</script> 8<script>dw(vcolon);</script></td><td headers="ds_power" nowrap>10.300 <script>dw(vdbmv);</script></td><td headers="ds_snr" nowrap>36.38<script>dw(vdb);</script></td></tr><tr><td headers="ds_channel" width="140" nowrap><script>dw(vs_channel);</script> 9<script>dw(vcolon);</script></td><td headers="ds_power" nowrap>10.300 <script>dw(vdbmv);</script></td><td headers="ds_snr" nowrap>36.61<script>dw(vdb);</script></td></tr><tr><td headers="ds_channel" width="140" nowrap><script>dw(vs_channel);</script> 10<script>dw(vcolon);</script></td><td headers="ds_power" nowrap>8.100 <script>dw(vdbmv);</script></td><td headers="ds_snr" nowrap>35.08<script>dw(vdb);</script></td></tr><tr><td headers="ds_channel" width="140" nowrap><script>dw(vs_channel);</script> 11<script>dw(vcolon);</script></td><td headers="ds_power" nowrap>8.400 <script>dw(vdbmv);</script></td><td headers="ds_snr" nowrap>35.59<script>dw(vdb);</script></td></tr><tr><td headers="ds_channel" width="140" nowrap><script>dw(vs_channel);</script> 12<script>dw(vcolon);</script></td><td headers="ds_power" nowrap>7.400 <script>dw(vdbmv);</script></td><td headers="ds_snr" nowrap>30.82<script>dw(vdb);</script></td></tr><tr><td headers="ds_channel" width="140" nowrap><script>dw(vs_channel);</script> 13<script>dw(vcolon);</script></td><td headers="ds_power" nowrap>6.800 <script>dw(vdbmv);</script></td><td headers="ds_snr" nowrap>32.32<script>dw(vdb);</script></td></tr><tr><td headers="ds_channel" width="140" nowrap><script>dw(vs_channel);</script> 14<script>dw(vcolon);</script></td><td headers="ds_power" nowrap>7.200 <script>dw(vdbmv);</script></td><td headers="ds_snr" nowrap>34.92<script>dw(vdb);</script></td></tr><tr><td headers="ds_channel" width="140" nowrap><script>dw(vs_channel);</script> 15<script>dw(vcolon);</script></td><td headers="ds_power" nowrap>6.900 <script>dw(vdbmv);</script></td><td headers="ds_snr" nowrap>34.48<script>dw(vdb);</script></td></tr><tr><td headers="ds_channel" width="140" nowrap><script>dw(vs_channel);</script> 16<script>dw(vcolon);</script></td><td headers="ds_power" nowrap>8.200 <script>dw(vdbmv);</script></td><td headers="ds_snr" nowrap>35.59<script>dw(vdb);</script></td></tr><tr><td headers="ds_channel" width="140" nowrap><script>dw(vs_channel);</script> 17<script>dw(vcolon);</script></td><td headers="ds_power" nowrap>6.900 <script>dw(vdbmv);</script></td><td headers="ds_snr" nowrap>34.48<script>dw(vdb);</script></td></tr><tr><td headers="ds_channel" width="140" nowrap><script>dw(vs_channel);</script> 18<script>dw(vcolon);</script></td><td headers="ds_power" nowrap>6.000 <script>dw(vdbmv);</script></td><td headers="ds_snr" nowrap>34.48<script>dw(vdb);</script></td></tr><tr><td headers="ds_channel" width="140" nowrap><script>dw(vs_channel);</script> 19<script>dw(vcolon);</script></td><td headers="ds_power" nowrap>5.900 <script>dw(vdbmv);</script></td><td headers="ds_snr" nowrap>34.48<script>dw(vdb);</script></td></tr><tr><td headers="ds_channel" width="140" nowrap><script>dw(vs_channel);</script> 20<script>dw(vcolon);</script></td><td headers="ds_power" nowrap>5.600 <script>dw(vdbmv);</script></td><td headers="ds_snr" nowrap>34.34<script>dw(vdb);</script></td></tr><tr><td headers="ds_channel" width="140" nowrap><script>dw(vs_channel);</script> 21<script>dw(vcolon);</script></td><td headers="ds_power" nowrap>5.500 <script>dw(vdbmv);</script></td><td headers="ds_snr" nowrap>34.34<script>dw(vdb);</script></td></tr><tr><td headers="ds_channel" width="140" nowrap><script>dw(vs_channel);</script> 22<script>dw(vcolon);</script></td><td headers="ds_power" nowrap>4.800 <script>dw(vdbmv);</script></td><td headers="ds_snr" nowrap>34.34<script>dw(vdb);</script></td></tr><tr><td headers="ds_channel" width="140" nowrap><script>dw(vs_channel);</script> 23<script>dw(vcolon);</script></td><td headers="ds_power" nowrap>3.700 <script>dw(vdbmv);</script></td><td headers="ds_snr" nowrap>33.83<script>dw(vdb);</script></td></tr><tr><td headers="ds_channel" width="140" nowrap><script>dw(vs_channel);</script> 24<script>dw(vcolon);</script></td><td headers="ds_power" nowrap>4.600 <script>dw(vdbmv);</script></td><td headers="ds_snr" nowrap>33.83<script>dw(vdb);</script></td></tr></tbody>						</table>
						<br/>
					</td>
				</tr>
			</table>
			<!-- Downstream Channel Information End -->
			<table class="nav bm_docsisWanDSChannel">
				<tr id="i_HR3">
					<td class="Item1">&nbsp;</td>
					<td class="Item2"></td>
					<td><hr class="std"></td>
				</tr>
			</table>
			<!-- Upstream Channel Information Start -->
			<table class="nav paramTable bm_docsisWanUPChannel">
				<tr>
					<td class="bwhead">
						<script>dw(vusch);</script>
					</td>
					<td class="bwhead1">&nbsp;</td>
					<td class="nav1">&nbsp;</td>
				</tr>
				<tr height="3px">
					<td class="Item1"></td>
					<td class="Item2"></td>
					<td></td>
				</tr>
				<tr>
					<td class="Item1"> </td>
					<td class="Item2"> </td>
					<td class="Item3">
						<table class="std" summary="this table shows upstream channel information">
							<thead><tr><th align="left" id="us_channel" width="140" nowrap><script>dw(vChannel);</script></th><th align="left" id="us_power" width="140" class="stdbold" nowrap><script>dw(vch_pwr);</script></th></tr></thead><tbody><tr>      <td headers="us_channel" width="140" nowrap><script>dw(vs_channel);</script>1      <script>dw(vcolon);</script></td>      <td headers="us_power" nowrap>41.250 <script>dw(vdbmv);</script></td></tr><tr>      <td headers="us_channel" width="140" nowrap><script>dw(vs_channel);</script>2      <script>dw(vcolon);</script></td>      <td headers="us_power" nowrap>41.250 <script>dw(vdbmv);</script></td></tr></tbody>						</table>
						<br/>
					</td>
				</tr>
			</table>
			<!-- Upstream Channel Information End -->
		</td>
		<td class="help">
		</td>
	</tr>
</table>
</form>
<table class="bottom">
	<tr>
		<td class="Footer1">&nbsp;</td>
		<td class="Footer2" id="refreshButton">
			<script>showRefresh("Docsis_system.php");</script>&nbsp; &nbsp;
		</td>
		<td class="Footer3">&nbsp;</td>
	</tr>
</table>

<table border="0" cellpadding="0" cellspacing="0">
	<tr>
		<td align="center">
			<font size="1" color="white">
				<script>dw(vcopyright);</script>
			</font>
		</td>
	</tr>
</table>


</div><!-- end tag for #contentDiv-->
</div><!-- end tag for #container-->
<script>
    $(document).ready(function() {
        setTimeout(function() {
            var $content = $("#contentDiv");

            // mode for wifi operating status: NotAvailable(0),Off(1),Remote(2),Local(3)
            var radio_opt = ["Local",
                             "Local"];

            var radio_msg = ['<tr><td class="Item1"></td><td class="Item2"></td><td class="Item3">\
                        <div class="fieldGroup">2.4GHz wireless interface is disabled in your cable modem.</div>\
                        <hr class="std"/></td></tr>', 
                             '<tr><td class="Item1"></td><td class="Item2"></td><td class="Item3">\
                        <div class="fieldGroup">5GHz wireless interface is disabled in your cable modem.</div>\
                        <hr class="std"/></td></tr>', 
                             '<tr><td class="Item1"></td><td class="Item2"></td><td class="Item3">\
                        <div class="fieldGroup">Both wireless interface are disabled or not available in your cable modem.</div>\
                        <hr class="std"/></td></tr>'];

            var isWiFiOff = (("NotAvailable"==radio_opt[0] || "Off"==radio_opt[0]) && ("NotAvailable"==radio_opt[1] || "Off"==radio_opt[1]));

            if ($("#id_WL_UICtrl .paramTable").length == 2) {
                $("#id_WL_UICtrl .paramTable").each(function(i){
                    if ("NotAvailable" == radio_opt[i]) {
                        $(this).hide();
                    }
                    else if ("Off" == radio_opt[i]) {
                        $(this).find("tr:not(:first)").hide();
                        $(this).append(radio_msg[i]);
                    }
                    else if ("Remote" == radio_opt[i]) {
                        $(this).find("*").prop("disabled", true);
                    }
                });
                if (isWiFiOff) {
                    $(".bottom").hide();
                }
            }
            else if (vwps==$("title").text() || vwacl==$("title").text() || vwgn==$("title").text()) {
                if (isWiFiOff) {
                    $(".paramTable tr:not(:first)").hide();
                    $(".paramTable").append(radio_msg[2]);
                    $(".bottom").hide();
                }
                else if ("Local"!=radio_opt[0] && "Local"!=radio_opt[1]) {
                    $(".paramTable *").prop("disabled", true);
                }
            }

            $content.show();
        }, 2);
    });

</script>

</body>
</html>
