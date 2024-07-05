function u(e) {
                    function t(e, t) {
                        return e << t | e >>> 32 - t
                    }
                    function n(e, t) {
                        var n, r, o, i, a;
                        return o = 2147483648 & e,
                        i = 2147483648 & t,
                        a = (1073741823 & e) + (1073741823 & t),
                        (n = 1073741824 & e) & (r = 1073741824 & t) ? 2147483648 ^ a ^ o ^ i : n | r ? 1073741824 & a ? 3221225472 ^ a ^ o ^ i : 1073741824 ^ a ^ o ^ i : a ^ o ^ i
                    }
                    function r(e, t, n) {
                        return e & t | ~e & n
                    }
                    function o(e, t, n) {
                        return e & n | t & ~n
                    }
                    function i(e, t, n) {
                        return e ^ t ^ n
                    }
                    function a(e, t, n) {
                        return t ^ (e | ~n)
                    }
                    function s(e, o, i, a, s, u, l) {
                        return e = n(e, n(n(r(o, i, a), s), l)),
                        n(t(e, u), o)
                    }
                    function u(e, r, i, a, s, u, l) {
                        return e = n(e, n(n(o(r, i, a), s), l)),
                        n(t(e, u), r)
                    }
                    function l(e, r, o, a, s, u, l) {
                        return e = n(e, n(n(i(r, o, a), s), l)),
                        n(t(e, u), r)
                    }
                    function c(e, r, o, i, s, u, l) {
                        return e = n(e, n(n(a(r, o, i), s), l)),
                        n(t(e, u), r)
                    }
                    function f(e) {
                        for (var t, n = e.length, r = n + 8, o, i = 16 * ((r - r % 64) / 64 + 1), a = new Array(i - 1), s = 0, u = 0; n > u; )
                            s = u % 4 * 8,
                            a[t = (u - u % 4) / 4] = a[t] | e.charCodeAt(u) << s,
                            u++;
                        return s = u % 4 * 8,
                        a[t = (u - u % 4) / 4] = a[t] | 128 << s,
                        a[i - 2] = n << 3,
                        a[i - 1] = n >>> 29,
                        a
                    }
                    function d(e) {
                        var t, n, r = "", o = "";
                        for (n = 0; 3 >= n; n++)
                            r += (o = "0" + (t = e >>> 8 * n & 255).toString(16)).substr(o.length - 2, 2);
                        return r
                    }
                    function p(e) {
                        // e = e.replace(/\r\n/g, "\n");
                        for (var t = "", n = 0; n < e.length; n++) {
                            var r = e.charCodeAt(n);
                            128 > r ? t += String.fromCharCode(r) : r > 127 && 2048 > r ? (t += String.fromCharCode(r >> 6 | 192),
               

                            t += String.fromCharCode(63 & r | 128)) : (t += String.fromCharCode(r >> 12 | 224),
                            t += String.fromCharCode(r >> 6 & 63 | 128),
                            t += String.fromCharCode(63 & r | 128))
                        }
                        return t
                    }
                    var h, m, y, v, g, b, _, w, S, x = [], M = 7, k = 12, L = 17, T = 22, O = 5, E = 9, C = 14, j = 20, P = 4, D = 11, Y = 16, A = 23, N = 6, I = 10, R = 15, H = 21, F;
                    for (x = f(e = p(e)),
                    b = 1732584193,
                    _ = 4023233417,
                    w = 2562383102,
                    S = 271733878,
                    h = 0; h < x.length; h += 16)
                        m = b,
                        y = _,
                        v = w,
                        g = S,
                        b = s(b, _, w, S, x[h + 0], 7, 3614090360),
                        S = s(S, b, _, w, x[h + 1], k, 3905402710),
                        w = s(w, S, b, _, x[h + 2], L, 606105819),
                        _ = s(_, w, S, b, x[h + 3], T, 3250441966),
                        b = s(b, _, w, S, x[h + 4], 7, 4118548399),
                        S = s(S, b, _, w, x[h + 5], k, 1200080426),
                        w = s(w, S, b, _, x[h + 6], L, 2821735955),
                        _ = s(_, w, S, b, x[h + 7], T, 4249261313),
                        b = s(b, _, w, S, x[h + 8], 7, 1770035416),
                        S = s(S, b, _, w, x[h + 9], k, 2336552879),
                        w = s(w, S, b, _, x[h + 10], L, 4294925233),
                        _ = s(_, w, S, b, x[h + 11], T, 2304563134),
                        b = s(b, _, w, S, x[h + 12], 7, 1804603682),
                        S = s(S, b, _, w, x[h + 13], k, 4254626195),
                        w = s(w, S, b, _, x[h + 14], L, 2792965006),
                        b = u(b, _ = s(_, w, S, b, x[h + 15], T, 1236535329), w, S, x[h + 1], 5, 4129170786),
                        S = u(S, b, _, w, x[h + 6], 9, 3225465664),
                        w = u(w, S, b, _, x[h + 11], C, 643717713),
                        _ = u(_, w, S, b, x[h + 0], j, 3921069994),
                        b = u(b, _, w, S, x[h + 5], 5, 3593408605),
                        S = u(S, b, _, w, x[h + 10], 9, 38016083),
                        w = u(w, S, b, _, x[h + 15], C, 3634488961),
                        _ = u(_, w, S, b, x[h + 4], j, 3889429448),
                        b = u(b, _, w, S, x[h + 9], 5, 568446438),
                        S = u(S, b, _, w, x[h + 14], 9, 3275163606),
                        w = u(w, S, b, _, x[h + 3], C, 4107603335),
                        _ = u(_, w, S, b, x[h + 8], j, 1163531501),
                        b = u(b, _, w, S, x[h + 13], 5, 2850285829),
                        S = u(S, b, _, w, x[h + 2], 9, 4243563512),
                        w = u(w, S, b, _, x[h + 7], C, 1735328473),
                        b = l(b, _ = u(_, w, S, b, x[h + 12], j, 2368359562), w, S, x[h + 5], 4, 4294588738),
                        S = l(S, b, _, w, x[h + 8], D, 2272392833),
                        w = l(w, S, b, _, x[h + 11], Y, 1839030562),
                        _ = l(_, w, S, b, x[h + 14], A, 4259657740),
                        b = l(b, _, w, S, x[h + 1], 4, 2763975236),
                        S = l(S, b, _, w, x[h + 4], D, 1272893353),
                        w = l(w, S, b, _, x[h + 7], Y, 4139469664),
                        _ = l(_, w, S, b, x[h + 10], A, 3200236656),
                        b = l(b, _, w, S, x[h + 13], 4, 681279174),
                        S = l(S, b, _, w, x[h + 0], D, 3936430074),
                        w = l(w, S, b, _, x[h + 3], Y, 3572445317),
                        _ = l(_, w, S, b, x[h + 6], A, 76029189),
                        b = l(b, _, w, S, x[h + 9], 4, 3654602809),
                        S = l(S, b, _, w, x[h + 12], D, 3873151461),
                        w = l(w, S, b, _, x[h + 15], Y, 530742520),
                        b = c(b, _ = l(_, w, S, b, x[h + 2], A, 3299628645), w, S, x[h + 0], 6, 4096336452),
                        S = c(S, b, _, w, x[h + 7], I, 1126891415),
                        w = c(w, S, b, _, x[h + 14], R, 2878612391),
                        _ = c(_, w, S, b, x[h + 5], H, 4237533241),
                        b = c(b, _, w, S, x[h + 12], 6, 1700485571),
                        S = c(S, b, _, w, x[h + 3], I, 2399980690),
                        w = c(w, S, b, _, x[h + 10], R, 4293915773),
                        _ = c(_, w, S, b, x[h + 1], H, 2240044497),
                        b = c(b, _, w, S, x[h + 8], 6, 1873313359),
                        S = c(S, b, _, w, x[h + 15], I, 4264355552),
                        w = c(w, S, b, _, x[h + 6], R, 2734768916),
                        _ = c(_, w, S, b, x[h + 13], H, 1309151649),
                        b = c(b, _, w, S, x[h + 4], 6, 4149444226),
                        S = c(S, b, _, w, x[h + 11], I, 3174756917),
                        w = c(w, S, b, _, x[h + 2], R, 718787259),
                        _ = c(_, w, S, b, x[h + 9], H, 3951481745),
                        b = n(b, m),
                        _ = n(_, y),
                        w = n(w, v),
                        S = n(S, g);
                    return (d(b) + d(_) + d(w) + d(S)).toLowerCase()
                }