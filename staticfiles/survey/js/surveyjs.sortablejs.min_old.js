/*!
 * surveyjs-widgets - Widgets for the SurveyJS library v1.0.9
 * Copyright (c) 2015-2017 Devsoft Baltic OÜ  - http://surveyjs.io/
 * License: MIT (http://www.opensource.org/licenses/mit-license.php)
 */
! function(e, t) {
    "object" == typeof exports && "object" == typeof module ? module.exports = t(require("sortablejs")) : "function" == typeof define && define.amd ? define("widgets/sortablejs", ["sortablejs"], t) : "object" == typeof exports ? exports["widgets/sortablejs"] = t(require("sortablejs")) : e["widgets/sortablejs"] = t(e.Sortable)
}(this, function(e) {
    return function(e) {
        function t(r) {
            if (n[r]) return n[r].exports;
            var a = n[r] = {
                i: r,
                l: !1,
                exports: {}
            };
            return e[r].call(a.exports, a, a.exports, t), a.l = !0, a.exports
        }
        var n = {};
        return t.m = e, t.c = n, t.d = function(e, n, r) {
            t.o(e, n) || Object.defineProperty(e, n, {
                configurable: !1,
                enumerable: !0,
                get: r
            })
        }, t.n = function(e) {
            var n = e && e.__esModule ? function() {
                return e.default
            } : function() {
                return e
            };
            return t.d(n, "a", n), n
        }, t.o = function(e, t) {
            return Object.prototype.hasOwnProperty.call(e, t)
        }, t.p = "", t(t.s = 12)
    }({
        12: function(e, t, n) {
            "use strict";

            function r(e) {
                var t = {
                    name: "sortablelist",
                    title: "Sortable list",
                    iconName: "icon-sortablelist",
                    widgetIsLoaded: function() {
                        return void 0 !== o.a
                    },
                    defaultJSON: {
                        choices: ["Item 1", "Item 2", "Item 3"]
                    },
                    areaStyle: "border: 1px solid #82b1ce; width:100%; min-height:50px; font-size:14px;",
                    itemStyle: "background-color:#82b1ce;color:#fff;margin:5px;padding:10px; font-size:14px;",
                    isFit: function(e) {
                        return "sortablelist" === e.getType()
                    },
                    htmlTemplate: "<div></div>",
                    activatedByChanged: function(t) {
                        e.JsonObject.metaData.addClass("sortablelist", [{
                            name: "hasOther",
                            visible: !1
                        }, {
                            name: "storeOthersAsComment",
                            visible: !1
                        }], null, "checkbox"), e.JsonObject.metaData.addProperty("sortablelist", {
                            name: "emptyText",
                            default: "Move items here."
                        })
                    },
                    afterRender: function(e, t) {
                        var n = this;
                        t.style.width = "100%";
                        var r = document.createElement("div"),
                            a = document.createElement("span"),
                            arrow_container = document.createElement("div"),
                            arrow_svg = document.createElement('i'),
                            i = document.createElement("div");

                        arrow_svg.className = "fas fa-arrow-up";
                        arrow_svg.style = "color: #8BB0CB; display: block; margin-top: 10px; margin-bottom: 10px; margin-left: auto; margin-right: auto; width: 50px;"
                        arrow_container.style = "width: 100%; height: 50px;";
                        arrow_container.appendChild(arrow_svg);
                        r.style.cssText = n.areaStyle, a.innerHTML = e.emptyText, r.appendChild(a), i.style.cssText = n.areaStyle, i.style.marginTop = "10px"
                        t.appendChild(r);
                        //t.appendChild(arrow_container);
                        t.appendChild(i);

                        var l = function(t) {
                                var n = e.value;
                                if (!Array.isArray(n)) return !1;
                                for (var r = 0; r < n.length; r++)
                                    if (n[r] == t) return !0;
                                return !1
                            },
                            s = !1,
                            d = function() {
                                if (!s) {
                                    r.innerHTML = "", r.appendChild(a), i.innerHTML = "";
                                    var t = !1;
                                    e.activeChoices.forEach(function(e) {
                                        var a = l(e.value);
                                        t = t || a;
                                        var o = a ? r : i,
                                            s = document.createElement("div");
                                        s.innerHTML = "<div style='" + n.itemStyle + "'>" + e.text + "</div>", s.dataset.value = e.value, o.appendChild(s)
                                    }), a.style.display = t ? "none" : ""
                                }
                            };
                        e.resultEl = o.a.create(r, {
                            animation: 150,
                            group: e.name,
                            onSort: function(t) {
                                var n = [];
                                if (1 === r.children.length) a.style.display = "";
                                else {
                                    a.style.display = "none";
                                    for (var o = 0; o < r.children.length; o++) void 0 !== r.children[o].dataset.value && n.push(r.children[o].dataset.value)
                                }
                                s = !0, e.value = n, s = !1
                            }
                        }), e.sourceEl = o.a.create(i, {
                            animation: 150,
                            group: e.name
                        }), e.valueChangedCallback = d, d()
                    },
                    willUnmount: function(e, t) {
                        e.resultEl.destroy(), e.sourceEl.destroy()
                    }
                };
                e.CustomWidgetCollection.Instance.addCustomWidget(t, "customtype")
            }
            Object.defineProperty(t, "__esModule", {
                value: !0
            });
            var a = n(13),
                o = n.n(a);
            "undefined" != typeof Survey && r(Survey), t.default = r
        },
        13: function(t, n) {
            t.exports = e
        }
    })
});
//# sourceMappingURL=sortablejs.min.js.map