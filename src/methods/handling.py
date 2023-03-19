def http_status_response(status_code):
	"""
	Unnecessarily long method for handling http status code responses
	returns are string descriptions based on the specific code received
	as per the documentation at https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
	"""

	if status_code == 100:
		return "Continue"
	elif status_code == 101:
		return "Swtiching Protocols"
	elif status_code == 102:
		return "Processing"
	elif status_code == 103:
		return "Early Hints"
	elif status_code == 200:
		return "OK"
	elif status_code == 201:
		return "Created"
	elif status_code == 202:
		return "Accepted"
	elif status_code == 203:
		return "Non-Authoritative Information"
	elif status_code == 204:
		return "No Content"
	elif status_code == 205:
		return "Reset Content"
	elif status_code == 206:
		return "Partial Content"
	elif status_code == 207:
		return "Multi-Status"
	elif status_code == 208:
		return "Already Reported"
	elif status_code == 226:
		return "IM Used"
	elif status_code == 300:
		return "Multiple Choices"
	elif status_code == 301:
		return "Moved Permanently"
	elif status_code == 302:
		return "Found"
	elif status_code == 303:
		return "See Other"
	elif status_code == 304:
		return "Not Modified"
	elif status_code == 305:
		return "Use Proxy"
	elif status_code == 306:
		return "Deprecated code"
	elif status_code == 307:
		return "Temporary Redirect"
	elif status_code == 308:
		return "Permanent Redirect"
	elif status_code == 400:
		return "Bad Request"
	elif status_code == 401:
		return "Unauthorized"
	elif status_code == 402:
		return "Payment Required "
	elif status_code == 403:
		return "Forbidden"
	elif status_code == 404:
		return "Not Found"
	elif status_code == 405:
		return "Method Not Allowed"
	elif status_code == 406:
		return "Not Acceptable"
	elif status_code == 407:
		return "Proxy Authentication Required"
	elif status_code == 408:
		return "Request Timeout"
	elif status_code == 409:
		return "Conflict"
	elif status_code == 410:
		return "Gone"
	elif status_code == 411:
		return "Length Required"
	elif status_code == 412:
		return "Precondition Failed"
	elif status_code == 413:
		return "Payload Too Large"
	elif status_code == 414:
		return "URI Too Long"
	elif status_code == 415:
		return "Unsupported Media Type"
	elif status_code == 416:
		return "Range Not Satisfiable"
	elif status_code == 417:
		return "Expectation Failed"
	elif status_code == 418:
		return "I'm a teapot"
	elif status_code == 421:
		return "Misdirected Request"
	elif status_code == 422:
		return "Unprocessable Content "
	elif status_code == 423:
		return "Locked"
	elif status_code == 424:
		return "Failed Dependency"
	elif status_code == 425:
		return "Too Early"
	elif status_code == 426:
		return "Upgrade Required"
	elif status_code == 428:
		return "Precondition Required"
	elif status_code == 429:
		return "Too Many Requests"
	elif status_code == 431:
		return "Request Header Fields Too Large"
	elif status_code == 451:
		return "Unavailable For Legal Reasons"
	elif status_code == 500:
		return "Internal Server Error"
	elif status_code == 501:
		return "Not Implemented"
	elif status_code == 502:
		return "Bad Gateway"
	elif status_code == 503:
		return "Service Unavailable"
	elif status_code == 504:
		return "Gateway Timeout"
	elif status_code == 505:
		return "HTTP Version Not Supported"
	elif status_code == 506:
		return "Variant Also Negotiates"
	elif status_code == 507:
		return "Insufficient Storage"
	elif status_code == 508:
		return "Loop Detected"
	elif status_code == 510:
		return "Not Extended"
	elif status_code == 511:
		return "Network Authentication Required"