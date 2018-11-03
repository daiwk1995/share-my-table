
/*
 * Don Routine v1.0.0
 * Released under the DON license
 */

    // food
    function cartel(x)              {
	    var page,curPage,total,totalPage;
	    curPage= $('#curPage').text();
	    totalPage = $('#totalPage').text()
	    console.log(curPage + '----' + totalPage);
	    if (x === 1 ){ page = 1;}
	    else if (x === 'l') { page = 1;}
	    else if (x === 'n') { page = curPage-1;}
	    else if (x === 'm') { page = parseInt(curPage) + 1;}
	    else{ page = totalPage;}
	    $("#getuname").text(Cookies.get('username'));
	    $.ajax(
	        "/food/categories/",
            {
                type: 'get',
                async:true,
                data:{
                    'page': page,
                    'size': 10,
                },
                dataType: 'json',
                beforeSend: function(request) {
                   request.setRequestHeader("Authorization",'token ' + Cookies.get('token'));
                },
                success: function(data){
                    if(data.count !== 0){
                        $('.list').find('*').remove();
                        for (let i = 0; i < data.results.length; i++){
                            $(".list").append(
                                "<div class='cate col-lg-offset-2 col-md-offset-2 col-sm-offset-2 col-xs-offset-2 row'>" +
                                "<a style='background-color:transparent; border: transparent;' href='/reci?category_id=" + data.results[i].id + "'><div class='cate_pho'></div>" +
                                "<span class='cate_te'>" + data.results[i].name +
                                "</span></a></div>"
                            )
                        }
                        curPage = page;
                          $.ajax(
                              "/food/categories/",
                              {
                                  type: 'get',
                                  async:true,
                                  dataType: 'json',
                                  success: function(data){
                                      total = data.count;
                                      if (total%10 === 0){
                                          totalPage = (total-(total%10))/10;
                                      }else {
                                          totalPage = (total-(total%10))/10 + 1;
                                      }
                                       $('#totalPage').text(totalPage);
                                      console.log('Total: ' + total +'---'+ totalPage);
                                  }
                              })
                        $('#curPage').text(curPage);
                        console.log(data.results);
                    }else{
                        alert(data.msg);
                        console.log("hah");
                        console.log(data.results);
                    }
                },
                error: function(data){
                    alert('Error');
                    console.log(data);
                }
            });
	};
	function recial(x)              {
	    let page,curPage,total,totalPage,re;
	    let str = '';
	    curPage= $('#curPage').text();
	    totalPage = $('#totalPage').text();
	    console.log(curPage + '----' + totalPage);
	    if (x === 1 ){ page = 1;}
	    else if (x === 'l') { page = 1;}
	    else if (x === 'n') { page = curPage-1;}
	    else if (x === 'm') { page = parseInt(curPage) + 1;}
	    else{ page = totalPage;}
	    var url= window.location.search;
        if(url.indexOf("?")!=-1){
          re = url.substr(url.indexOf("=")+1);
        };
         console.log('Re:' + url + '++++' +re)
        $("#getuname").text(Cookies.get('username'));
        $.ajax(
            "/food/recipes/",
            {
                type: 'get',
                async:true,
                data:{
                    'category_id': re,
                    'page': page,
                    'size': 10,
                },
                dataType: 'json',
                beforeSend: function(request) {
                    request.setRequestHeader("Authorization",'token ' + Cookies.get('token'));
                    },
                success: function(data){
                    if(data.count !== 0){
                        for (let i = 0; i < data.results.length; i++){
                            str += "<div class='col-lg-12 col-xs-12 col-sm-12 col-md-12 row btn center-block' style='margin: 10px auto;background-color: #DEB887; border-radius: 10px; text-align: left'><h3 style='margin-left: 10px;'>";
                            str += data.results[i].title;
                            str += "</h3><span style='margin-left: 10px; color: whitesmoke;'>Calories：";
                            str += data.results[i].calories;
                            str += "</span><span style='margin-left: 10px; color: whitesmoke;'>Fat：";
                            str += data.results[i].fat;
                            str += "</span><span style='margin-left: 10px; color: whitesmoke;'>Protein: ";
                            str += data.results[i].protein;
                            str += "</span><span style='margin-left: 10px; color: whitesmoke;'>Rating: ";
                            str += data.results[i].rating;
                            str += "</span><span style='margin-left: 10px; color: whitesmoke;'>Sodium: ";
                            str += data.results[i].sodium;
                            str += "</span><br/><button style='margin: 5px auto 10px 10px; color: whitesmoke;width: 100px;height: 25px;background-color: #8a6d3b;border-radius: 10px;border: 0px solid' onclick='getingre(";
                            str += data.results[i].r_id;
                            str += ");'>ingredient<span class='caret'></span></button><div style='display: none' id='ingre";
                            str += data.results[i].r_id;
                            str += "'><hr/>";
                            for (let j = 0 ; j < data.results[i].ingredients.length; j++){
                                str += "<div style='margin-bottom: 10px;'><span style='margin-left: 10px; color: whitesmoke;'>";
                                str += data.results[i].ingredients[j].detail;
                                str += "</span>";
                                str += "<button style='float: right; margin-right: 10px; width: 50px; height: 20px; background-color: #8a6d3b; border-radius: 10px; border: 0px solid;' onclick='itemadd(";
                                str += data.results[i].ingredients[j].id;
                                str += ")'>Add</button>";
                                str += "<input id='weight";
                                str += data.results[i].ingredients[j].id;
                                str += "' style='float: right; margin-right: 30px;width: 70px;height: 20px;background-color: whitesmoke;border-radius: 5px;border: 0px solid;text-align: center;' type='number' id='setweight'/>";
                                str += "<span style='float: right;margin-right: 10px;'>Weight: </span></div>";
                            }
                            str += "</div></div>";
                        }
                        $('.reclist').find('*').remove();
                        $(".reclist").append(str);
                        curPage = page;
                        $.ajax(
                            "/food/recipes/",
                            {
                                type: 'get',
                                async:true,
                                data:{
                                    'category_id': re,
                                },
                                dataType: 'json',
                                success: function(data){
                                    total = data.count;
                                    if (total%10 === 0){
                                        totalPage = (total-(total%10))/10;
                                    }else {
                                        totalPage = (total-(total%10))/10 + 1;
                                    }
                                    $('#totalPage').text(totalPage);
                                    console.log('Total: ' + total +'---'+ totalPage);
                                }
                            })
                        $('#curPage').text(curPage);
                        console.log(data.results);
                    }else{
                        alert(data.msg);
                        console.log(data.results);
                    }
                },
                error: function(data){
                    alert('Please Login');
                    console.log(data);
                }
            });
    };
	function bag(x)                  {


        var str = '';
        $("#getuname").text(Cookies.get('username'));
        $(".pe_name").append(Cookies.get('username'));
        str += "<tr style='font-size: 18px;font-weight: 700;'>";
        str += "<th class='row col-lg-offset-1 col-md-offset-1 col-lg-3 col-md-3' style='text-align: center;'>NAME</th>";
        str += "<th class='row col-lg-3 col-md-3' style='text-align: center;'>EXPIRE TIME</th>";
        str += "<th class='row col-lg-3 col-md-3' style='text-align: center;'>WEIGHT</th>";
        str += "<th class='row col-lg-2 col-md-2' style='text-align: center;'>";
        str += "<button style='width: 35px; height: 25px; border: 0px; background-color:transparent;' onclick='bagadditemframe()'><img style='width: 25px; height: 25px;' src='s/img/add.png'/></button></th></tr>";

        str += "<tr id='bagadditem' style='display: none; font-size: 16px; text-align: center; height: 45px;'>";
        str += "<td class='row col-lg-offset-1 col-md-offset-1 col-lg-3 col-md-3'>";
        str += "<input id='bagaddname' type='text' style='width: 120px; border: 1px solid wheat; border-radius: 5px; color: #8a6d3b; text-align: center;'/>"
        str += "</td><td class='row col-lg-3 col-md-3'>";
        str += "<input id='bagaddtime' type='date' style='width: 120px; border: 1px solid wheat; border-radius: 5px; color: #8a6d3b; text-align: center;'/>"
        str += "</td><td class='row col-lg-3 col-md-3'>";
        str += "<input id='bagaddweight' type='number' style='width: 120px; border: 1px solid wheat; border-radius: 5px; color: #8a6d3b; text-align: center;'/>"
        str += "</td><td class='row col-lg-2 col-md-2'>";
        str += "<button style='float: right; width: 50px; height: 30px; border: 0px; background-color: transparent;' onclick='bagadditemframe()'><img style='width: 25px; height: 25px;' src='s/img/over.png'/></button>";
        str += "<button style='float: right; margin-right: 10px; width: 50px; height: 30px; border: 0px; background-color: transparent;' onclick='bagadditem()'><img style='width: 25px; height: 25px;' src='s/img/save.png'/></button></td></tr>";

        var st = '';
        if (x===2){
    st = $('#searchbag').val();
}
        $.ajax(
            "/user/bag_items/",
            {
                type: 'get',
                async: true,
                data: {
                    search: st
                    // search: 'tomato'
                },
                dataType: 'json',
                beforeSend: function (request) {
                    request.setRequestHeader("Authorization", 'token ' + Cookies.get('token'));
                },
                success: function (data) {
                    if (data.count !== 0) {
                        for (let i = 0; i < data.results.length; i++) {
                            str += "<tr style='font-size: 16px; text-align: center; height: 45px;'>";
                            str += "<td class='row col-lg-offset-1 col-md-offset-1 col-lg-3 col-md-3'>";
                            str += data.results[i].ingredients.name;
                            str += "</td><td class='row col-lg-3 col-md-3'>";

                            str += "<span id='bag11_"
                            str += data.results[i].id;
                            str += "' style='display:;'>";
                            str += data.results[i].expire_time;
                            str += "</span>";

                            str += "<input id='bag12_";
                            str += data.results[i].id;
                            str += "' type='date' style='display:none; width: 120px; border: 1px solid wheat; border-radius: 5px; color: #8a6d3b; text-align: center; background-color: rgba(250,250,230,0.7);'/>";

                            str += "</td><td class='row col-lg-3 col-md-3'>";

                            str += "<span id='bag21_";
                            str += data.results[i].id;
                            str += "' style='display:;'>";
                            str += data.results[i].weight;
                            str += "</span>";

                            str += "<input id='bag22_";
                            str += data.results[i].id;
                            str += "' type='number' style='display:none; width: 80px; border: 1px solid wheat; border-radius: 5px; color: #8a6d3b; text-align: center; background-color: rgba(250,250,230,0.7);' placeholder='";
                            str += data.results[i].weight;
                            str +=  "'/>";

                            str += "</td><td class='row col-lg-2 col-md-2'>";

                            str += "<button style='float: right; width: 50px; height: 30px; border: 0px; background-color: transparent;' onclick='bagitemdel(";
                            str += data.results[i].id;
                            str += ")'><img style='width: 30px; height: 30px;' src='s/img/del.png'/></button>";

                            str += "<button id='bag31_";
                            str += data.results[i].id;
                            str += "' style='display:; float: right; margin-right: 10px; width: 50px; height: 30px; border: 0px; background-color: transparent;' onclick='bagupdateitemframe(";
                            str += data.results[i].id;
                            str += ")'><img style='width: 30px; height: 30px;' src='s/img/edit.png'/></button>";

                            str += "<button id='bag32_";
                            str += data.results[i].id;
                            str += "' style='display:none; float: right; margin-right: 10px; width: 50px; height: 30px; border: 0px; background-color: transparent;' onclick='bagupdateitem(";
                            str += data.results[i].id;
                            str += ",";
                            str += data.results[i].ingredients.id;
                            str += ")'><img style='width: 30px; height: 30px;' src='s/img/save.png'/></button>";

                            str += "</td></tr>";
                        }
                        $('.baglist').find('*').remove();
                        $(".baglist").append(str);
                        console.log(data.results);
                    } else {
                        $(".baglist").append(str);
                        alert('No Data');
                        console.log("hah");
                        console.log(data.results);
                    }
                },
                error: function (data) {
                    alert('Please Login');
                    console.log(data);
                },
            });
    };

	function bagadditemframe()      {
        s = document.getElementById('bagadditem');
        if (s.style.display === "none") {
            s.style.display = '';
        } else {
            s.style.display = 'none';
        }
    };
	function bagadditem()           {
        var name = $('#bagaddname').val();
        var time = $('#bagaddtime').val();
        var weight = $('#bagaddweight').val();
        $.ajax('/food/categories/',
            {
                type: 'get',
                async: true,
                data: {
                    search: name,
                },
                dataType: 'json',
                beforeSend: function (request) {
                    request.setRequestHeader("Authorization", 'token ' + Cookies.get('token'));
                },
                success: function (data) {
                    if (data.count >= 1) {
                        $.ajax(
                            "/user/bag_item/",
                            {
                                type: 'post',
                                async: true,
                                data: {
                                    'weight': weight,
                                    'expire_time': time,
                                    'ingredients': data.results[0].id
                                },
                                dataType: 'json',
                                beforeSend: function (request) {
                                    request.setRequestHeader("Authorization", 'token ' + Cookies.get('token'));
                                },
                                success: function () {
                                    reframe('Add Success');
                                    window.location.reload();
                                },
                                error: function (data) {
                                    reframe('Add Default');
                                }
                            })
                    } else {
                        reframe('Sorry,There is no the food material.');
                    }
                },
                error: function (data) {
                    console.log(data);
                }
            })
    };

	function bagupdateitemframe(x)  {
        for (var i = 1; i < 4; i++) {
              document.getElementById('bag' + i + '1_' + x).style.display = 'none';
              document.getElementById('bag' + i + '2_' + x).style.display = '';
        }
    };
	function bagupdateitem(x,y)     {
        var time = $('#bag12_' + x).val();
        var weight = $('#bag22_' + x).val();

        console.log(':..' + $('#bag11_' + x).text());
        console.log(':...' + $('#bag21_' + x).text());
        console.log(x + ':::' + y + '-----' + time + '----' + weight);
        $.ajax(
            '/user/bag_item/' + x + '/',
            {
                type: 'put',
                async: true,
                data: {
                    'weight': weight,
                    'expire_time': time,
                    'ingredients': y
                },
                dataType: 'json',
                beforeSend: function (request) {
                    request.setRequestHeader("Authorization", 'token ' + Cookies.get('token'));
                },
                success: function () {
                    reframe('Update Success');
                    window.location.reload();
                },
                error: function (data) {
                    reframe('Update Default');
                },
                complete: function () {
                    for (var i = 1; i < 4; i++) {
                        document.getElementById('bag' + i + '1_' + x).style.display = '';
                        document.getElementById('bag' + i + '2_' + x).style.display = 'none';
                    }
                }
            })
    };

    function bagitemdel(x)          {
        var r=confirm("Sure Delete?")
        if (r==true){
            $.ajax(
	         "/user/bag_item/"+ x +"/",
            {
                type: 'delete',
                async:true,
                data:{
                    id: x
                },
                dataType: 'json',
                beforeSend: function(request) {
                    request.setRequestHeader("Authorization",'token ' + Cookies.get('token'));
                },
                complete: function () {
                    window.location.reload();
                }
            });
        } else {
            console.log('Cencer');
        }
    };
    function itemadd(x)             {
        $.ajax(
            "/user/bag_item/",
            {
                type: 'post',
                async:true,
                data:{
                    'weight': $('#weight' + x).val(),
                    'expire_time': '2018-10-20 10:10:10',
                    'ingredients': x
                },
                dataType: 'json',
                beforeSend: function(request) {
                   request.setRequestHeader("Authorization",'token ' + Cookies.get('token'));
                },
                 success: function () {
                    alert('Add Success');
                    console.log('HA');
                },
                error: function(data){
                    alert('Add Default');
                    console.log(data);
                }
            })

        };
    function search(x) {
        if (x === 1) {
            window.location.href = '/searchresult?search=' + $('#searchcon').val();
            return 0;
        } else if (x === 2) {
            var st = $('#searchbag').val();
            console.log('------>>>' + st)
            $('searchbaritem').text('Search Result : ' + st);
            bag(2);
        }
    };


    function searchresult()         {
        var re;
        var str = '';
        var url= window.location.search;
        if(url.indexOf("?")!=-1){
          re = url.substr(url.indexOf("=")+1);
        };
        console.log('Re:' + url + '++++' +re)

        $('#seares').text('Search Result For : ' + re);
	    $.ajax(
	        "/food/recipes/",
            {
                type: 'get',
                async:true,
                data:{
                    'search': re,
                },
                dataType: 'json',
                beforeSend: function(request) {
                    request.setRequestHeader("Authorization",'token ' + Cookies.get('token'));
                },
                success: function(data){
                    if(data.count !== 0){
                        for (let i = 0; i < data.results.length; i++){
                            str += "<div class='col-lg-12 col-xs-12 col-sm-12 col-md-12 row btn center-block' style='margin: 10px auto;background-color: #DEB887; border-radius: 10px; text-align: left'><span style='margin-left: 10px; font-size: 26px; color: #2E2D3C;'>";
                            str += data.results[i].title;
                            str += "</span><br/><span style='margin-left: 10px; color: whitesmoke;'>Calories：";
                            str += data.results[i].calories;
                            str += "</span><span style='margin-left: 10px; color: whitesmoke;'>Fat：";
                            str += data.results[i].fat;
                            str += "</span><span style='margin-left: 10px; color: whitesmoke;'>Protein: ";
                            str += data.results[i].protein;
                            str += "</span><span style='margin-left: 10px; color: whitesmoke;'>Rating: ";
                            str += data.results[i].rating;
                            str += "</span><span style='margin-left: 10px; color: whitesmoke;'>Sodium: ";
                            str += data.results[i].sodium;
                            str += "</span><br/><button style='margin: 5px auto 10px 10px; color: whitesmoke;width: 100px;height: 25px;background-color: #8a6d3b;border-radius: 10px;border: 0px solid' onclick='getingre(";
                            str += data.results[i].r_id;
                            str += ");'>ingredient<span class='caret'></span></button><div style='display: none' id='ingre";
                            str += data.results[i].r_id;
                            str += "'><hr/>";
                            for (let j = 0 ; j < data.results[i].ingredients.length; j++){
                                str += "<div style='margin-bottom: 5px;'><span style='margin-left: 10px; color: whitesmoke;'>";
                                str += data.results[i].ingredients[j].detail;
                                str += "</span></div>";


                                // str += "<button style='float: right; margin-right: 10px; width: 50px; height: 20px; background-color: #8a6d3b; border-radius: 10px; border: 0px solid;' onclick='itemadd(";
                                // str += data.results[i].ingredients[j].id;
                                // str += ")'>Add</button>";
                                // str += "<input id='weight";
                                // str += data.results[i].ingredients[j].id;
                                // str += "' style='float: right; margin-right: 30px;width: 70px;height: 20px;background-color: whitesmoke;border-radius: 5px;border: 0px solid;text-align: center;' type='number' id='setweight'/>";
                                // str += "<span style='float: right;margin-right: 10px;'>Weight: </span></div>";
                            }
                            str += "</div></div>";
                        }
                        $('.sealist').find('*').remove();
                        $(".sealist").append(str);
                        console.log(data.results);
                    }else{
                        alert(data.msg);
                    }
                },
                error: function(data){
                    alert('Please Login');
                    console.log(data);
                }
            });
    };
    function getingre(id)           {
        const s = eval("ingre"+id);
        if (s.style.display == "none")
        {
            eval("ingre"+id+".style.display=\"\"; ");
        }else{
            eval("ingre"+id+".style.display=\"none\";");
        }
    };

    //invitation
    function invitation(x)          {
        let page, curPage, total, totalPage;
        let str = '';
        curPage= $('#curPage').text();
	    totalPage = $('#totalPage').text()
	    console.log(curPage + '----' + totalPage);
	    if (x === 1 ){ page = 1;}
	    else if (x === 'l') { page = 1;}
	    else if (x === 'n') { page = curPage-1;}
	    else if (x === 'm') { page = parseInt(curPage) + 1;}
	    else{ page = totalPage;}
	    $("#getuname").text(Cookies.get('username'));
        $.ajax(
            "/invitation/messages/",
            {
                type: 'get',
                async:true,
                data:{
                    'page': page,
                    'size': 10,
                },
                dataType: 'json',
                beforeSend: function(request) {
                    request.setRequestHeader("Authorization",'token ' + Cookies.get('token'));
                    },
                success: function(data){
                    if(data.count !== 0){
                        if(data.count !== 0){
                            for (let i = 0; i < data.results.length; i++){
                                str += "<div style='position:relative;margin-top: 20px; width:100%;height:90px;background-color:#DEB887;border-radius:10px;'><br/><span style='margin: 0 auto auto 10px;font-size: 24px;'>";
                                str += data.results[i].content;
                                str += "</span><br/><span style='margin-left: 10px;color: whitesmoke;font-size: 16px;'>";
                                str += data.results[i].user.username;
                                str += "</span><span style='margin-left: 10px;color: whitesmoke;font-size: 16px;'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";
                                str += data.results[i].created_time;
                                str += "</span><button style='float: right;margin-right: 10px;width: 80px;height: 26px;background-color: #8a6d3b;border-radius: 10px;border: 0px solid' onclick='messagedel(";
                                str += data.results[i].id;
                                str += ")'>Delete</button>";
                                str += "<button style='float: right; margin-right: 10px; width: 80px;height: 26px;background-color: #8a6d3b;border-radius: 10px;border: 0px solid' onclick='setcomment(";
                                str += data.results[i].id;
                                str += ")'>Comment</button></div>";

                                str += "<div style='margin-top: 5px;height: auto; display: none;' id='comm";
                                str += data.results[i].id;
                                str += "'><input style='margin-left: 10px;height: auto; width: 400px; border-radius: 3px; border: 0px solid; text-align: center; color: black;' type='text' id='commcon";
                                str += data.results[i].id;
                                str += "' value=''/>";
                                str += "<button style=' margin-left: 10px;height: 24px;width: 100px; border-radius: 10px; border: 0px solid; background-color: #8a6d3b' onclick='sendcomm(";
                                str += data.results[i].id;
                                str += ")'>Send</button>";
                                str += "</div>";

                                if(data.results[i].message_answered.length>0) {
                                    str += "<div style='margin-top: 5px;height: auto'>";
                                    for (let j = 0; j < data.results[i].message_answered.length; j++) {
                                        str += "<div style='margin-bottom: 3px;'>";
                                        str += "<span style='margin-left: 20px; color: blue;font-size: 16px;'>";
                                        str += data.results[i].message_answered[j].user.username;
                                        if (data.results[i].message_answered[j].answer_to === null) {
                                            str += '';
                                        }else {
                                            str += "</span>";
                                            str += "<span style='margin-left: 3px; color: whitesmoke;font-size: 16px;'> answer </span>";
                                            str += "<span style='margin-left: 3px; color: blue;font-size: 16px;'>";
                                            str += data.results[i].message_answered[j].answer_to.user.username;
                                        }
                                        str += " : </span>";
                                        str += "<span style='margin-left: 3px; color: whitesmoke;font-size: 16px;'>";
                                        str += data.results[i].message_answered[j].content;
                                        str += "</span>";

                                        str += "<a style='float: right; margin-right: 10px; color: blue;font-size: 16px;' href='javascript:commentdel(";
                                        str += data.results[i].message_answered[j].id;
                                        str += ");'>Delete</a>";

                                        str += "<a style='float: right; margin-right: 10px; color: blue;font-size: 16px;' href='javascript:commenttoanswer(";
                                        str += data.results[i].message_answered[j].id;
                                        str += ");'>Comment</a>";

                                        str += "<div style='margin-top: 5px;height: auto; display: none;' id='commtoans";
                                        str += data.results[i].message_answered[j].id;
                                        str += "'><input style='margin-left: 10px;height: auto; width: 400px; border-radius: 3px; border: 0px solid; text-align: center; color: black;' type='text' id='commtocon";
                                        str += data.results[i].message_answered[j].id;
                                        str += "' value=''/>";
                                        str += "<button style=' margin-left: 10px;height: 24px;width: 100px; border-radius: 10px; border: 0px solid; background-color: #8a6d3b' onclick='commenttoans(";
                                        str += data.results[i].message_answered[j].id;
                                        str += ",";
                                        str += data.results[i].id;
                                        str += ")'>Send</button>";
                                        str += "</div>"
                                    }
                                    str += "</div>";
                                }
                                str += "</div>";
                            }
                        }
                        $(".invitationlist").append(str)
                        curPage = page;
                        $.ajax(
                            "/invitation/messages/",
                            {
                                type: 'get',
                                async:true,
                                dataType: 'json',
                                beforeSend: function(request) {
                                    request.setRequestHeader("Authorization",'token ' + Cookies.get('token'));
                                    },
                                success: function(data){
                                    total = data.count;
                                    if (total%10 === 0){
                                        totalPage = (total-(total%10))/10;
                                    }else {
                                        totalPage = (total-(total%10))/10 + 1;
                                    }
                                    $('#totalPage').text(totalPage);
                                    console.log('Total: ' + total +'---'+ totalPage);
                                }
                            })
                        $('#curPage').text(curPage);
                        console.log(data.results);
                    }else{
                        alert('No Data');
                        console.log(data.results);
                    }
                },
                error: function(data){
                    alert('Please Login');
                    console.log(data);
                }
            });
    };
	function messagedel(x)          {
	    console.log('----->' + x);
	    var r=confirm("Sure Delete?")
        if (r==true)
        {
	     $.ajax(
	         "/invitation/message/" + x + "/",
            {
                type: 'delete',
                async:true,
                data:{
                    id: x
                },
                beforeSend: function(request) {
                    request.setRequestHeader("Authorization",'token ' + Cookies.get('token'));
                },
                complete: function () {
                    window.location.reload();
                }
            });
        } else {
            console.log('Cencer');
        }
    };
    function messageadd()           {
         console.log($('#cont').val());
         if ($('#cont').val() === null){
             alert('Please Input Content');
         } else {
             $.ajax(
                 "/invitation/message/",
                 {
                     type: 'post',
                     async: true,
                     data: {
                         'content': $('#cont').val(),
                     },
                     dataType: 'json',
                     beforeSend: function (req) {
                         req.setRequestHeader("Authorization", 'token ' + Cookies.get('token'));
                     },
                     success: function () {
                         console.log('Add Success......');
                         window.location.href = document.referrer;
                         // window.location.reload();
                     },
                     error: function (data) {
                         alert('Add Default');
                         console.log(data);
                     }
                 })
         }
    };
    function sendcomm(x)            {
        console.log($('#commcon'+x).val());
        $.ajax(
            "/invitation/answer/",
            {
                type: 'post',
                async:true,
                data:{
                    'content': $('#commcon'+x).val(),
                    'message':  x,
                },
                dataType: 'json',
                beforeSend: function(request) {
                    request.setRequestHeader("Authorization",'token ' + Cookies.get('token'));
                },
                success: function(data) {
                    window.location.reload();
                    },
                error: function(data){
                    window.location.reload();
                    alert('Comment Error');
                }
            });
    };
    function setcomment(id)         {
        const s = eval("comm"+id);
        if (s.style.display == "none")
        {
            eval("comm"+id+".style.display=\"\"; ");
        }else{
            eval("comm"+id+".style.display=\"none\";");
        }
    };
    function commenttoanswer(id)    {
             const s = eval("commtoans"+id);
        if (s.style.display == "none")
        {
            eval("commtoans"+id+".style.display=\"\"; ");
        }else{
            eval("commtoans"+id+".style.display=\"none\";");
        }
    };
    function commentdel(x)          {
        console.log('----->' + x);
	    var r=confirm("Sure Delete?")
        if (r==true) {
            $.ajax(
                "/invitation/answer/" + x + "/",
                {
                    type: 'delete',
                    async:true,
                    data:{
                        id: x
                    },
                beforeSend: function(request) {
                    request.setRequestHeader("Authorization",'token ' + Cookies.get('token'));
                },
                complete: function () {
                    window.location.reload();
                }
            });
        } else {
            console.log('Cencer');
        }
    };
    function commenttoans(x,y)      {
  console.log($('#commtocon'+x).val());
        $.ajax(
            "/invitation/answer/",
            {
                type: 'post',
                async:true,
                data:{
                    'answer_to': x,
                    'content': $('#commtocon'+x).val(),
                    'message':  y,
                },
                dataType: 'json',
                beforeSend: function(request) {
                    request.setRequestHeader("Authorization",'token ' + Cookies.get('token'));
                },
                success: function(data) {
                    window.location.reload();
                    },
                error: function(data){
                    window.location.reload();
                    alert('Comment Error');
                }
            });
    };

    //user
    function login()                {
        console.log($("#username").val());
        console.log($("#password").val());
        var username, first_name, last_name, token;
        if ($("#username").val() === '') {
            reframe("THE USERNAME CANNOT BE EMPTY");
        } else if ($("#password").val() === '') {
            reframe("THE PASSWORD CANNOT BE EMPTY");
        } else {
            $.ajax(
                "/user/login/",
                {
                    type: 'post',
                    async: true,
                    data: {
                        'username': $("#username").val(),
                        'password': $("#password").val(),
                    },
                    dataType: 'json',
                    success: function (data) {
                        if (data.user != null) {
                            Cookies.set('username', data.user.username);
                            Cookies.set('first_name', data.user.first_name);
                            Cookies.set('last_name', data.user.last_name);
                            Cookies.set('token', data.token);
                            window.location.href = "/second"
                        } else {
                            reframe('USERNAME OR PASSWORD ERROR');
                        }
                    },
                    error: function (data) {
                        reframe('USERNAME OR PASSWORD ERROR...');
                    }
                });
        }
    };
	function logout()               {
        var r = confirm("Sure Logout?")
        if (r == true) {
            $.ajax(
                "/user/logout/",
                {
                    type: 'post',
                    async: true,
                });
            Cookies.remove('username');
            Cookies.remove('first_name');
            Cookies.remove('last_name');
            Cookies.remove('token');
            window.location.href = "/";
        } else {
            console.log('Cancer');
        }
    };
	function regedit()              {
	    if ($("#username").val() === '') {
	        reframe("THE USERNAME CANNOT BE EMPTY");
	    } else if ($("#password").val() === '') {
	        reframe("THE PASSWORD CANNOT BE EMPTY");
	    } else if ($("#first_name").val() === '') {
	        reframe("THE FIRST NAME CANNOT BE EMPTY");
	    } else if ($("#last_name").val() === '') {
	        reframe("THE LAST NAME CANNOT BE EMPTY");
	    } else {
	        $.ajax(
	            "/user/register/",
                {
                    type: 'post',
                    async:true,
                    data:{
                        username: $("#username").val(),
                        password:  $("#password").val(),
                        first_name: $("#first_name").val(),
                        last_name: $("#last_name").val()
                    },
                    dataType: 'json',
                    success: function(data){
                        if(data.username != null){
                            reframe('REGEDIT SUCCESS');
                            window.location.href='/signin';
                        }else {
                            reframe('REGEDIT ERROR');
                        }
                        },
                    error: function(){
                        reframe('REGEDIT ERROR...');
                    }
                });
	    }
	};
	function setting()              {
         $('#setting').find('*').remove();
         $('#setting').append("<div class='inventory'>Personal Setting</div><hr/>" +
             "<div><div style='24px;'>Reset Password: </div><br/>" +
             "<div style='margin: 10px auto;width: 300px;height: auto;'>" +
             "<span>Old Passwords:</span><br/><input class='repasswd center-block' type='password' id='oldpwd' value=''/></div>" +

             "<div style='margin: 10px auto;width: 300px;height: auto;'>" +
             "<span>New Passwords:</span><br/><input class='repasswd center-block' type='password' id='newpwd' value=''/></div>" +

             "<div style='margin: 10px auto;width: 300px;height: auto;'>" +
             "<span>Re Enter:</span><br/><input class='repasswd center-block' type='password' id='repwd' value=''/></div>" +

             "<button style=' float:right;margin:30px 10px auto auto;height: 45px;width: 100px;background-color: white;border-radius: 10px;border: 2px solid burlywood;color: #C0A16B;font-size: 20px;' onclick='repassword(1)'>Save</button></div>" +
             "<button style=' float:right;margin:30px 10px auto auto;height: 45px;width: 100px;background-color: white;border-radius: 10px;border: 2px solid burlywood;color: #C0A16B;font-size: 20px;' onclick='window.location.reload();'>Cancer</button></div>"
        );
    };
    function repassword(x)          {
        var oldpwd = $('#oldpwd').val();
        var newpwd = $('#newpwd').val();
        var repwd = $('#repwd').val();
        if (newpwd !== repwd){
            alert("'Re Enter' Is No Match")
        }else {
            $.ajax(
                "/user/password/" + x + "/",
                {
                    type: 'put',
                    async: true,
                    data: {
                        'id': x,
                        'old_password': oldpwd,
                        'new_password': newpwd
                    },
                    beforeSend: function (request) {
                        request.setRequestHeader("Authorization", 'token ' + Cookies.get('token'));
                    },
                    complete: function () {
                        alert('Reset Success...');
                        window.location.reload();
                    }
                });
        }
    };
	function second()               {
          $("#getuname").text(Cookies.get('username'));
    };

	function reframe(x)             {
        console.log(x);
        layer.msg(x, {
            offset: 't',
            time: 3000
        });
    };








































