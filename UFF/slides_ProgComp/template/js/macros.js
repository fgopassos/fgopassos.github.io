// Image with style. Any list of css properties is valid. Usage example:
// ![:imageS width:50%;opacity:0.7](image.jpg)
remark.macros.imageS = function (style) {
  var url = this;
  return '<img src="' + url + '" style="' + style + '" />';
};

// Simpler image declaration macro. The only parameter is the width (declared
// in any unit, including percentage). Usage example:
// ![:image 50%](image.jpg)
remark.macros.image = function (width) {
  var url = this;
  return '<img src="' + url + '" style="width: ' + width + '" />';
};

// ![:iframe height, width](url)
remark.macros.iframe = function (height, width) {
  var url = this;
  return '<iframe src="' + url + '" height="' + height + '" width="' + width + '"></iframe>';
}

// ![:column width](content)
remark.macros.column = function(width) {

    return '<div style="width: ' + width + '; float: left;">' + window.remark.convert(this) + "</div>";
}

// Creates a "block" on the slide. The content is passed as the parameter
// between parenthesis. If you want the block to contain a title, it should be
// placed alone in the first line of the parameter. The remaining lines are the
// markdown that will define the content of the block. Examples of how this
// macro should be used:
// ![:block](A Possibly Long Title, with many elements. This is still the title.
//* An item of a list.
//* A second item
//)
// ![:block](
//This block will have no title, just this sentence.
//)
remark.macros.block = function () {

  var ret = "";
  var title = "";
  var i;
  var md;

  args = this.split("\n");
  title = args[0];
  args.splice(0, 1);
  md = args.join('\n');

  ret = '<table class="block">';
  if (title != "") {

    ret += '<thead>';
    ret += '<tr>';
    ret += '<td>' + title + '</td>';
    ret += '</tr>';
    ret += '</thead>';
  }
  ret += '<tbody>';
  ret += '<tr>';
  ret += '<td>' + window.remark.convert(md) + '</td>';
  ret += '</tr>';
  ret += '</table>';
  return ret;
};

// Creates a cover slide. Expects four parameters: an event, a title for the
// the presentation, the author name, and the logo.
// Parameters are specified as separated
// lines within the parenthesis argument. Example:
// ![:cover](
// Programação de Computadores
// Aula 1: Introdução à Disciplina
// Fernanda Passos
// logo.svg
// )
// The first argument may be placed in the same line as the macro name. Empty
// lines are ignored.
// The background image is currently hardcoded, but may be changed
// by simply replacing the file "img/bg.png".
remark.macros.cover = function() {

  var ret = "";
  var i;

  args = this.split("\n");
  for (i = 0; i < args.length; i++) {

    if (args[i] == "") args.splice(i, 1);
  }

  if (args.length < 4) console.log("Cover Macro: Not enough argments. Render may not be correct.")
  else if (args.length > 4) console.log("Cover Macro: Too many arguments. Render may not be correct.")

  var where = args[0];
  var what = args[1];
  var author = args[2];
  var logo = args[3];

  ret += '<span class="cover-slide-logo"><img src="' + logo + '"></img></span>';
  ret += '<div style="width: 90%; position: absolute; top: 60%; left: 5%; color: #FFF; text-align: center;">';
  ret += '<table class="cover-slide-table">';
  ret += '  <tr>';
  ret += '    <td style="width: 50%; padding-right: 2%;"><hr style="border: 0; border-top: 2px solid #FFF;"></td>';
  ret += '    <td style="white-space: nowrap; font-size: 22px; padding-left: 1px;">' + where + '</td>';
  ret += '    <td style="width: 50%; padding-left: 2%;"><hr style="border: 0; border-top: 2px solid #FFF;"></td>';
  ret += '  </tr>';
  ret += '</table>';
  ret += '<div style="font-size: 41px; margin-top: 1%; margin-bottom: 2%;">' + what + '</div>';
  ret += '<hr style="border: 0; border-top: 2px solid #FFF;">';
  ret += '<span style="font-size: 22px;">' + author + '</span>';
  ret += '</div>';

  return ret;
}

// ![:translate](md)
// Translates the markdown passed as argument to html.
remark.macros.translate = function() {

    console.log(window.remark.convert(this));
    return window.remark.convert(this);
}

// ![:dagre width, height](graphDefinition)
remark.macros.dagre = function(width, height) {

    var g = graphlibDot.read(this);
    g.graph().marginx = 20;
    g.graph().marginy = 20;

    if (typeof window.dagreGraphs === 'undefined') window.dagreGraphs = [];
    var idx = window.dagreGraphs.push(g) - 1;

    return '<svg idx="' + idx + '" height="' + height + '" width="' + width + '"><g/></svg>';
}

remark.macros.tableEx = function() {

    var src = this;

    var token = {
      pipe : 1,
      plus : 2,
      minus: 3,
      colon: 4,
      semiColon : 5,
      openBracket : 6,
      closeBracket : 7,
      text : 8,
      classId: 9,
      eol : 10,
      eof : 11
    };

    var isLetter = function(c) {
      return c.toLowerCase() != c.toUpperCase();
    }

    var isNumber = function(c) {
      return c.match(/[a-z]/i);
    }

    var nextToken = function(src, start) {

      var i = start;
      var end = src.length;
      var state = 0;
      var secToken = "";

      while (i < end) {

        var ch = src.charAt(i);

        switch(state) {

          case 0:

            // One char tokens.
            if (ch == '|') return {where: i + 1, token: token.pipe, secToken: null};
            if (ch == '+') return {where: i + 1, token: token.plus, secToken: null};
            if (ch == '-') return {where: i + 1, token: token.minus, secToken: null};
            if (ch == ':') return {where: i + 1, token: token.colon, secToken: null};
            if (ch == ';') return {where: i + 1, token: token.semiColon, secToken: null};
            if (ch == '{') return {where: i + 1, token: token.openBracket, secToken: null};
            if (ch == '}') return {where: i + 1, token: token.closeBracket, secToken: null};
            if (ch == '\n') return {where: i + 1, token: token.eol, secToken: null};

            // Perhaps windows line break.
            if (ch == '\r') {

              state = 1;
              break ;
            }

            // If we got thus far, it is either an identifier or text. Either
            // way, we need to store the actual string as a secondary token.
            secToken = secToken + ch;

            // Identifier or text
            if (isLetter(ch)) {

              state = 2;
              break ;
            }

            // Anything else: text.
            state = 3;

          case 1:

            // Windows line-break
            if (ch == '\n') return {where: i + 1, token: token.eol, tokSec: null};

            // Anything else: text
            secToken = secToken + ch;
            state = 3;
            break ;

          case 2:

            // End of an identifier. We are cheating a little bit here, knowing
            // that in the syntatic grammar identifiers are always followed by
            // '}' or ':'. Any changes to the syntatic grammar must be reflected
            // here.
            if (ch == '}' || ch == ':') {

              // Remeber: ch is not part of the current token (it belogs to the
              // next). So we return the adequate value of where.
              return {where: i, token: token.classId, tokSec: secToken};
            }


            // Still seems to be an identifier.
            if (isLetter(ch) || isNumber(ch) || ch == '-' || ch == '_') {

              secToken = secToken + ch;
              break ;
            }

            // If we got here, then it must not be an identifier. It is certainly
            // text, but it may have ended here. Check for a bunch of other
            // characters.
            if (ch == '|' || ch == '+' || ch == '+' || ch == '-' || ch == ':' || ch == ';' || ch == '{' || ch == '}' || ch == '\n' || ch == '\r') {

              return {where: i, token: token.text, secToken: null};
            }

            // Well, it is a text that keeps going. Update secondary token and
            // migrate to the state that handles text. Care must be taken with
            // escaped special chars. There is a special state to handle those.
            if (ch == '\\') state = 4;
            else state = 3;

            secToken = secToken + ch;
            break ;

          case 3:

            // It is certainly text, but it may have ended here. Check for a
            // bunch of other characters.
            if (ch == '|' || ch == '+' || ch == '+' || ch == '-' || ch == ':' || ch == ';' || ch == '{' || ch == '}' || ch == '\n' || ch == '\r') {

              return {where: i, token: token.text, secToken: null};
            }

            // More text to come. Again, we take special care of escaped chars.
            if (ch == '\\') state = 4;
            else state = 3;

            secToken = secToken + ch;
            break ;

          case 4:

            // This is a dummy sub-state of the text token search. We only get
            // here after a backslash (which only happens within text). Our only
            // job here is to update the secondary token and check if ch is
            // another backslash or anything else.
            if (ch != '\\') state = 3;

            secToken = secToken + ch;
            break ;
        }

        i = i + 1;
      }

      return {where: i, token: token.eof, tokSec: null};
    }

    var tokenInfo;
    var i = 0;
    var state = 0;

    while (true) {

      tokenInfo = nextToken(src, i);
      i = tokenInfo.where;

        switch (state) {

          case 0:

            if (tokenInfo.token == token.eof) {
              // Empty table specification. Nothing to output.

              return ;
            }

            if (tokenInfo.token == token.pipe)
            break;

        }
    }
}
