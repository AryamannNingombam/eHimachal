var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g;
    return g = { next: verb(0), "throw": verb(1), "return": verb(2) }, typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (_) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
;
;
function getMessage(alert) {
    return "\n    <div class=\"alert alert-" + alert.type + " alert-dismissible fade show\" role=\"alert\">\n  " + alert.message + "\n  <button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\">\n    <span aria-hidden=\"true\">&times;</span>\n  </button>\n</div>";
}
;
var SendingContactRequest = /** @class */ (function () {
    function SendingContactRequest(url) {
        this.url = url;
    }
    SendingContactRequest.prototype.sendRequest = function (body) {
        return __awaiter(this, void 0, void 0, function () {
            var cookie, request, response;
            return __generator(this, function (_a) {
                switch (_a.label) {
                    case 0:
                        cookie = this.getCookie('csrftoken');
                        return [4 /*yield*/, fetch(this.url, {
                                method: 'POST',
                                headers: {
                                    'Content-Type': 'application/json',
                                    'X-CSRFToken': cookie
                                },
                                body: JSON.stringify(body)
                            })];
                    case 1:
                        request = _a.sent();
                        return [4 /*yield*/, request.json()];
                    case 2:
                        response = _a.sent();
                        return [2 /*return*/, response.successful];
                }
            });
        });
    };
    SendingContactRequest.prototype.getCookie = function (name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
                ;
            }
            ;
        }
        ;
        return cookieValue;
    };
    return SendingContactRequest;
}());
;
//MAIN LOGIC
var successMessage = { message: '<strong>Hello!</strong> We have successfully <strong>got your message</strong> and would try to contact you as soon as possible.<strong>Thanks!</strong>', type: 'success' };
var warningMessage = { message: "<strong>Hello!</strong>  We <strong> coudn't send your request </strong> as you might have entered some invalid credentials. Please enter correct credentials to send the request. <strong>Thanks!</strong>", type: 'warning' };
var errorMessage = { message: '<strong>Error!</strong> We <strong>could not send your request </strong> due to an internal server error. We apologize for the inconvenience caused. <strong>Sorry!</strong>', type: 'danger' };
var request = new SendingContactRequest('http://127.0.0.1:8000/contact-request/');
var alertSpan = document.getElementById('alertSpan');
var submitButton = document.getElementById('submitButton');
submitButton.addEventListener('click', function (e) {
    var emailInput = document.getElementById('email');
    var messageInput = document.getElementById('content');
    var email = emailInput.value;
    var message = messageInput.value;
    e.preventDefault();
    var body = { email_address: email, message: message };
    request.sendRequest(body).then(function (successful) {
        if (successful) {
            var responseAlert = getMessage(successMessage);
            alertSpan.innerHTML = responseAlert;
        }
        else {
            var responseAlert = getMessage(warningMessage);
            alertSpan.innerHTML = responseAlert;
        }
        ;
    })["catch"](function (error) {
        var responseAlert = getMessage(errorMessage);
        alertSpan.innerHTML = responseAlert;
    });
    emailInput.value = '';
    messageInput.value = '';
    window.scroll(0, 0);
});
