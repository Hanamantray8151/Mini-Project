const express = require('express');
const bodyParser = require('body-parser');

const app = express();

app.set("view engine", "ejs");
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(express.static("public"));

app.get("/",function(req,res){
    res.render("gym1");
});

app.listen(process.env.PORT || 3000,function(){
    console.log("App is listenning on 3000");
})