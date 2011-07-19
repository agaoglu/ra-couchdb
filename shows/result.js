function(doc, req) {  
  var Mustache = require("lib/mustache");
  var md5 = require("lib/md5").hex;
  var ctx = {
    form: true
  };
  if (req.query.password) {
    if (!doc) {
      ctx.idnErr = "Wrong ID number";
    } else if (doc.passwd != md5(req.query.password)) {
      ctx.passErr = "Wrong password";
    } else {
      ctx.form = false;
      ctx.doc = doc;
    }
  }
  return Mustache.to_html(this.templates.result, ctx);
}
