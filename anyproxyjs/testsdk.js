var fs = require("fs");
var moment = require("moment");
var iconv = require('iconv-lite');
var charset = 'utf-8';
var dateTime = moment().format("YYYY_MM_DD_HH_mm_ss");
var path = "d:/untitled2/log";
var log = path + "/" + dateTime + "_interfaceLog.log";
console.log(log);

var arr=["sdk-actlog.dftoutiao.com","sdk-newsapi.dftoutiao.com","sdknativeadv.dftoutiao.com",
    "nativeadv.dftoutiao.com","lianmeng.dftoutiao.com","mini.eastday.com","sdk-columns.dftoutiao.com"];

function contains(arr, obj)
{
    var i = arr.length;
    while (i--)
    {
        if (arr[i] === obj)
        {
            return true;
        }
    }
    return false;
}

module.exports = {
  *beforeSendResponse(requestDetail, responseDetail)
    {
    const newRequest = iconv.decode(requestDetail.requestData, charset);
    //var reqbody = iconv.decode(reqBody, charset);
    const newResponse = iconv.decode(responseDetail.response.body, charset);
    //console.info(requestDetail.requestOptions.hostname);

    if (contains(arr,requestDetail.requestOptions.hostname)){
    //if (requestDetail.requestOptions.hostname == "lianmeng.dftoutiao.com" || requestDetail.requestOptions.hostname == "nativeadv.dftoutiao.com") {
        fs.appendFileSync(log, new Date().toLocaleString() + " \nurl: " + requestDetail.url + "\n", 'utf-8', function (err) {
            if (err) throw err;
            console.log('url is saved!');
        });

        fs.appendFileSync(log, "requestbody:\n[",'utf-8' );
        var reqbody = iconv.decode(newRequest, charset);
        var arry = reqbody.toString().split("&");
        for (var i = 0, l = arry.length; i < l; i++) {
            if (i==arry.length-1)
               fs.appendFileSync(log, arry[i] + "]\n");
            else
                fs.appendFileSync(log, arry[i] + "\n");
        }

        //fs.appendFileSync(log, "-----------write request end----------------------" + "\n\n");

        //fs.appendFileSync(log, "request：" + newRequest + "\n ", 'utf-8', function (err) {
        //    if (err) throw err;
        //    console.log('requestData is saved!');
        //});
        fs.appendFileSync(log, "response:\n" + newResponse + "\n\n", 'utf-8', function (err) {
            if (err) throw err;
            console.log('responseData is saved!');
        });

    }
    }
};