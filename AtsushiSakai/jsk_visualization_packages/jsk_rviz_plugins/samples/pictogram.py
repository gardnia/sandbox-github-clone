#!/usr/bin/env python

import rospy
import tf
from jsk_rviz_plugins.msg import Pictogram
from random import random
rospy.init_node("pictogram_sample")
p = rospy.Publisher("/pictogram", Pictogram)

r = rospy.Rate(0.1)

pictograms = ["phone",
              "mobile",
              "mouse",
              "address",
              "mail",
              "paper-plane",
              "pencil",
              "feather",
              "attach",
              "inbox",
              "reply",
              "reply-all",
              "forward",
              "user",
              "users",
              "add-user",
              "vcard",
              "export",
              "location",
              "map",
              "compass",
              "direction",
              "hair-cross",
              "share",
              "shareable",
              "heart",
              "heart-empty",
              "star",
              "star-empty",
              "thumbs-up",
              "thumbs-down",
              "chat",
              "comment",
              "quote",
              "home",
              "popup",
              "search",
              "flashlight",
              "print",
              "bell",
              "link",
              "flag",
              "cog",
              "tools",
              "trophy",
              "tag",
              "camera",
              "megaphone",
              "moon",
              "palette",
              "leaf",
              "note",
              "beamed-note",
              "new",
              "graduation-cap",
              "book",
              "newspaper",
              "bag",
              "airplane",
              "lifebuoy",
              "eye",
              "clock",
              "mic",
              "calendar",
              "flash",
              "thunder-cloud",
              "droplet",
              "cd",
              "briefcase",
              "air",
              "hourglass",
              "gauge",
              "language",
              "network",
              "key",
              "battery",
              "bucket",
              "magnet",
              "drive",
              "cup",
              "rocket",
              "brush",
              "suitcase",
              "traffic-cone",
              "globe",
              "keyboard",
              "browser",
              "publish",
              "progress-3",
              "progress-2",
              "progress-1",
              "progress-0",
              "light-down",
              "light-up",
              "adjust",
              "code",
              "monitor",
              "infinity",
              "light-bulb",
              "credit-card",
              "database",
              "voicemail",
              "clipboard",
              "cart",
              "box",
              "ticket",
              "rss",
              "signal",
              "thermometer",
              "water",
              "sweden",
              "line-graph",
              "pie-chart",
              "bar-graph",
              "area-graph",
              "lock",
              "lock-open",
              "logout",
              "login",
              "check",
              "cross",
              "squared-minus",
              "squared-plus",
              "squared-cross",
              "circled-minus",
              "circled-plus",
              "circled-cross",
              "minus",
              "plus",
              "erase",
              "block",
              "info",
              "circled-info",
              "help",
              "circled-help",
              "warning",
              "cycle",
              "cw",
              "ccw",
              "shuffle",
              "back",
              "level-down",
              "retweet",
              "loop",
              "back-in-time",
              "level-up",
              "switch",
              "numbered-list",
              "add-to-list",
              "layout",
              "list",
              "text-doc",
              "text-doc-inverted",
              "doc",
              "docs",
              "landscape-doc",
              "picture",
              "video",
              "music",
              "folder",
              "archive",
              "trash",
              "upload",
              "download",
              "save",
              "install",
              "cloud",
              "upload-cloud",
              "bookmark",
              "bookmarks",
              "open-book",
              "play",
              "paus",
              "record",
              "stop",
              "ff",
              "fb",
              "to-start",
              "to-end",
              "resize-full",
              "resize-small",
              "volume",
              "sound",
              "mute",
              "flow-cascade",
              "flow-branch",
              "flow-tree",
              "flow-line",
              "flow-parallel",
              "left-bold",
              "down-bold",
              "up-bold",
              "right-bold",
              "left",
              "down",
              "up",
              "right",
              "circled-left",
              "circled-down",
              "circled-up",
              "circled-right",
              "triangle-left",
              "triangle-down",
              "triangle-up",
              "triangle-right",
              "chevron-left",
              "chevron-down",
              "chevron-up",
              "chevron-right",
              "chevron-small-left",
              "chevron-small-down",
              "chevron-small-up",
              "chevron-small-right",
              "chevron-thin-left",
              "chevron-thin-down",
              "chevron-thin-up",
              "chevron-thin-right",
              "left-thin",
              "down-thin",
              "up-thin",
              "right-thin",
              "arrow-combo",
              "three-dots",
              "two-dots",
              "dot",
              "cc",
              "cc-by",
              "cc-nc",
              "cc-nc-eu",
              "cc-nc-jp",
              "cc-sa",
              "cc-nd",
              "cc-pd",
              "cc-zero",
              "cc-share",
              "cc-remix",
              "db-logo",
              "db-shape",
              "github",
              "c-github",
              "flickr",
              "c-flickr",
              "vimeo",
              "c-vimeo",
              "twitter",
              "c-twitter",
              "facebook",
              "c-facebook",
              "s-facebook",
              "google+",
              "c-google+",
              "pinterest",
              "c-pinterest",
              "tumblr",
              "c-tumblr",
              "linkedin",
              "c-linkedin",
              "dribbble",
              "c-dribbble",
              "stumbleupon",
              "c-stumbleupon",
              "lastfm",
              "c-lastfm",
              "rdio",
              "c-rdio",
              "spotify",
              "c-spotify",
              "qq",
              "instagram",
              "dropbox",
              "evernote",
              "flattr",
              "skype",
              "c-skype",
              "renren",
              "sina-weibo",
              "paypal",
              "picasa",
              "soundcloud",
              "mixi",
              "behance",
              "google-circles",
              "vk",
              "smashing",
              "fa-adjust",
"fa-adn",
"fa-align-center",
"fa-align-justify",
"fa-align-left",
"fa-align-right",
"fa-ambulance",
"fa-anchor",
"fa-android",
"fa-angellist",
"fa-angle-double-down",
"fa-angle-double-left",
"fa-angle-double-right",
"fa-angle-double-up",
"fa-angle-down",
"fa-angle-left",
"fa-angle-right",
"fa-angle-up",
"fa-apple",
"fa-archive",
"fa-area-chart",
"fa-arrow-circle-down",
"fa-arrow-circle-left",
"fa-arrow-circle-o-down",
"fa-arrow-circle-o-left",
"fa-arrow-circle-o-right",
"fa-arrow-circle-o-up",
"fa-arrow-circle-right",
"fa-arrow-circle-up",
"fa-arrow-down",
"fa-arrow-left",
"fa-arrow-right",
"fa-arrow-up",
"fa-arrows",
"fa-arrows-alt",
"fa-arrows-h",
"fa-arrows-v",
"fa-asterisk",
"fa-at",
"fa-automobile",
"fa-backward",
"fa-ban",
"fa-bank",
"fa-bar-chart",
"fa-bar-chart-o",
"fa-barcode",
"fa-bars",
"fa-beer",
"fa-behance",
"fa-behance-square",
"fa-bell",
"fa-bell-o",
"fa-bell-slash",
"fa-bell-slash-o",
"fa-bicycle",
"fa-binoculars",
"fa-birthday-cake",
"fa-bitbucket",
"fa-bitbucket-square",
"fa-bitcoin",
"fa-bold",
"fa-bolt",
"fa-bomb",
"fa-book",
"fa-bookmark",
"fa-bookmark-o",
"fa-briefcase",
"fa-btc",
"fa-bug",
"fa-building",
"fa-building-o",
"fa-bullhorn",
"fa-bullseye",
"fa-bus",
"fa-cab",
"fa-calculator",
"fa-calendar",
"fa-calendar-o",
"fa-camera",
"fa-camera-retro",
"fa-car",
"fa-caret-down",
"fa-caret-left",
"fa-caret-right",
"fa-caret-square-o-down",
"fa-caret-square-o-left",
"fa-caret-square-o-right",
"fa-caret-square-o-up",
"fa-caret-up",
"fa-cc",
"fa-cc-amex",
"fa-cc-discover",
"fa-cc-mastercard",
"fa-cc-paypal",
"fa-cc-stripe",
"fa-cc-visa",
"fa-certificate",
"fa-chain",
"fa-chain-broken",
"fa-check",
"fa-check-circle",
"fa-check-circle-o",
"fa-check-square",
"fa-check-square-o",
"fa-chevron-circle-down",
"fa-chevron-circle-left",
"fa-chevron-circle-right",
"fa-chevron-circle-up",
"fa-chevron-down",
"fa-chevron-left",
"fa-chevron-right",
"fa-chevron-up",
"fa-child",
"fa-circle",
"fa-circle-o",
"fa-circle-o-notch",
"fa-circle-thin",
"fa-clipboard",
"fa-clock-o",
"fa-close",
"fa-cloud",
"fa-cloud-download",
"fa-cloud-upload",
"fa-cny",
"fa-code",
"fa-code-fork",
"fa-codepen",
"fa-coffee",
"fa-cog",
"fa-cogs",
"fa-columns",
"fa-comment",
"fa-comment-o",
"fa-comments",
"fa-comments-o",
"fa-compass",
"fa-compress",
"fa-copy",
"fa-copyright",
"fa-credit-card",
"fa-crop",
"fa-crosshairs",
"fa-css3",
"fa-cube",
"fa-cubes",
"fa-cut",
"fa-cutlery",
"fa-dashboard",
"fa-database",
"fa-dedent",
"fa-delicious",
"fa-desktop",
"fa-deviantart",
"fa-digg",
"fa-dollar",
"fa-dot-circle-o",
"fa-download",
"fa-dribbble",
"fa-dropbox",
"fa-drupal",
"fa-edit",
"fa-eject",
"fa-ellipsis-h",
"fa-ellipsis-v",
"fa-empire",
"fa-envelope",
"fa-envelope-o",
"fa-envelope-square",
"fa-eraser",
"fa-eur",
"fa-euro",
"fa-exchange",
"fa-exclamation",
"fa-exclamation-circle",
"fa-exclamation-triangle",
"fa-expand",
"fa-external-link",
"fa-external-link-square",
"fa-eye",
"fa-eye-slash",
"fa-eyedropper",
"fa-facebook",
"fa-facebook-square",
"fa-fast-backward",
"fa-fast-forward",
"fa-fax",
"fa-female",
"fa-fighter-jet",
"fa-file",
"fa-file-archive-o",
"fa-file-audio-o",
"fa-file-code-o",
"fa-file-excel-o",
"fa-file-image-o",
"fa-file-movie-o",
"fa-file-o",
"fa-file-pdf-o",
"fa-file-photo-o",
"fa-file-picture-o",
"fa-file-powerpoint-o",
"fa-file-sound-o",
"fa-file-text",
"fa-file-text-o",
"fa-file-video-o",
"fa-file-word-o",
"fa-file-zip-o",
"fa-files-o",
"fa-film",
"fa-filter",
"fa-fire",
"fa-fire-extinguisher",
"fa-flag",
"fa-flag-checkered",
"fa-flag-o",
"fa-flash",
"fa-flask",
"fa-flickr",
"fa-floppy-o",
"fa-folder",
"fa-folder-o",
"fa-folder-open",
"fa-folder-open-o",
"fa-font",
"fa-forward",
"fa-foursquare",
"fa-frown-o",
"fa-futbol-o",
"fa-gamepad",
"fa-gavel",
"fa-gbp",
"fa-ge",
"fa-gear",
"fa-gears",
"fa-gift",
"fa-git",
"fa-git-square",
"fa-github",
"fa-github-alt",
"fa-github-square",
"fa-gittip",
"fa-glass",
"fa-globe",
"fa-google",
"fa-google-plus",
"fa-google-plus-square",
"fa-google-wallet",
"fa-graduation-cap",
"fa-group",
"fa-h-square",
"fa-hacker-news",
"fa-hand-o-down",
"fa-hand-o-left",
"fa-hand-o-right",
"fa-hand-o-up",
"fa-hdd-o",
"fa-header",
"fa-headphones",
"fa-heart",
"fa-heart-o",
"fa-history",
"fa-home",
"fa-hospital-o",
"fa-html5",
"fa-ils",
"fa-image",
"fa-inbox",
"fa-indent",
"fa-info",
"fa-info-circle",
"fa-inr",
"fa-instagram",
"fa-institution",
"fa-ioxhost",
"fa-italic",
"fa-joomla",
"fa-jpy",
"fa-jsfiddle",
"fa-key",
"fa-keyboard-o",
"fa-krw",
"fa-language",
"fa-laptop",
"fa-lastfm",
"fa-lastfm-square",
"fa-leaf",
"fa-legal",
"fa-lemon-o",
"fa-level-down",
"fa-level-up",
"fa-life-bouy",
"fa-life-buoy",
"fa-life-ring",
"fa-life-saver",
"fa-lightbulb-o",
"fa-line-chart",
"fa-link",
"fa-linkedin",
"fa-linkedin-square",
"fa-linux",
"fa-list",
"fa-list-alt",
"fa-list-ol",
"fa-list-ul",
"fa-location-arrow",
"fa-lock",
"fa-long-arrow-down",
"fa-long-arrow-left",
"fa-long-arrow-right",
"fa-long-arrow-up",
"fa-magic",
"fa-magnet",
"fa-mail-forward",
"fa-mail-reply",
"fa-mail-reply-all",
"fa-male",
"fa-map-marker",
"fa-maxcdn",
"fa-meanpath",
"fa-medkit",
"fa-meh-o",
"fa-microphone",
"fa-microphone-slash",
"fa-minus",
"fa-minus-circle",
"fa-minus-square",
"fa-minus-square-o",
"fa-mobile",
"fa-mobile-phone",
"fa-money",
"fa-moon-o",
"fa-mortar-board",
"fa-music",
"fa-navicon",
"fa-newspaper-o",
"fa-openid",
"fa-outdent",
"fa-pagelines",
"fa-paint-brush",
"fa-paper-plane",
"fa-paper-plane-o",
"fa-paperclip",
"fa-paragraph",
"fa-paste",
"fa-pause",
"fa-paw",
"fa-paypal",
"fa-pencil",
"fa-pencil-square",
"fa-pencil-square-o",
"fa-phone",
"fa-phone-square",
"fa-photo",
"fa-picture-o",
"fa-pie-chart",
"fa-pied-piper",
"fa-pied-piper-alt",
"fa-pinterest",
"fa-pinterest-square",
"fa-plane",
"fa-play",
"fa-play-circle",
"fa-play-circle-o",
"fa-plug",
"fa-plus",
"fa-plus-circle",
"fa-plus-square",
"fa-plus-square-o",
"fa-power-off",
"fa-print",
"fa-puzzle-piece",
"fa-qq",
"fa-qrcode",
"fa-question",
"fa-question-circle",
"fa-quote-left",
"fa-quote-right",
"fa-ra",
"fa-random",
"fa-rebel",
"fa-recycle",
"fa-reddit",
"fa-reddit-square",
"fa-refresh",
"fa-remove",
"fa-renren",
"fa-reorder",
"fa-repeat",
"fa-reply",
"fa-reply-all",
"fa-retweet",
"fa-rmb",
"fa-road",
"fa-rocket",
"fa-rotate-left",
"fa-rotate-right",
"fa-rouble",
"fa-rss",
"fa-rss-square",
"fa-rub",
"fa-ruble",
"fa-rupee",
"fa-save",
"fa-scissors",
"fa-search",
"fa-search-minus",
"fa-search-plus",
"fa-send",
"fa-send-o",
"fa-share",
"fa-share-alt",
"fa-share-alt-square",
"fa-share-square",
"fa-share-square-o",
"fa-shekel",
"fa-sheqel",
"fa-shield",
"fa-shopping-cart",
"fa-sign-in",
"fa-sign-out",
"fa-signal",
"fa-sitemap",
"fa-skype",
"fa-slack",
"fa-sliders",
"fa-slideshare",
"fa-smile-o",
"fa-soccer-ball-o",
"fa-sort",
"fa-sort-alpha-asc",
"fa-sort-alpha-desc",
"fa-sort-amount-asc",
"fa-sort-amount-desc",
"fa-sort-asc",
"fa-sort-desc",
"fa-sort-down",
"fa-sort-numeric-asc",
"fa-sort-numeric-desc",
"fa-sort-up",
"fa-soundcloud",
"fa-space-shuttle",
"fa-spinner",
"fa-spoon",
"fa-spotify",
"fa-square",
"fa-square-o",
"fa-stack-exchange",
"fa-stack-overflow",
"fa-star",
"fa-star-half",
"fa-star-half-empty",
"fa-star-half-full",
"fa-star-half-o",
"fa-star-o",
"fa-steam",
"fa-steam-square",
"fa-step-backward",
"fa-step-forward",
"fa-stethoscope",
"fa-stop",
"fa-strikethrough",
"fa-stumbleupon",
"fa-stumbleupon-circle",
"fa-subscript",
"fa-suitcase",
"fa-sun-o",
"fa-superscript",
"fa-support",
"fa-table",
"fa-tablet",
"fa-tachometer",
"fa-tag",
"fa-tags",
"fa-tasks",
"fa-taxi",
"fa-tencent-weibo",
"fa-terminal",
"fa-text-height",
"fa-text-width",
"fa-th",
"fa-th-large",
"fa-th-list",
"fa-thumb-tack",
"fa-thumbs-down",
"fa-thumbs-o-down",
"fa-thumbs-o-up",
"fa-thumbs-up",
"fa-ticket",
"fa-times",
"fa-times-circle",
"fa-times-circle-o",
"fa-tint",
"fa-toggle-down",
"fa-toggle-left",
"fa-toggle-off",
"fa-toggle-on",
"fa-toggle-right",
"fa-toggle-up",
"fa-trash",
"fa-trash-o",
"fa-tree",
"fa-trello",
"fa-trophy",
"fa-truck",
"fa-try",
"fa-tty",
"fa-tumblr",
"fa-tumblr-square",
"fa-turkish-lira",
"fa-twitch",
"fa-twitter",
"fa-twitter-square",
"fa-umbrella",
"fa-underline",
"fa-undo",
"fa-university",
"fa-unlink",
"fa-unlock",
"fa-unlock-alt",
"fa-unsorted",
"fa-upload",
"fa-usd",
"fa-user",
"fa-user-md",
"fa-users",
"fa-video-camera",
"fa-vimeo-square",
"fa-vine",
"fa-vk",
"fa-volume-down",
"fa-volume-off",
"fa-volume-up",
"fa-warning",
"fa-wechat",
"fa-weibo",
"fa-weixin",
"fa-wheelchair",
"fa-wifi",
"fa-windows",
"fa-won",
"fa-wordpress",
"fa-wrench",
"fa-xing",
"fa-xing-square",
"fa-yahoo",
"fa-yelp",
"fa-yen",
"fa-youtube",
"fa-youtube-play",
"fa-youtube-square"]

br=tf.TransformBroadcaster()

counter = 0
while not rospy.is_shutdown():
    msg = Pictogram()
    msg.action = Pictogram.JUMP_ONCE
    msg.header.frame_id = "/base_link"
    msg.header.stamp = rospy.Time.now()
    msg.pose.position.z = 1.6
    msg.pose.orientation.w = 0.7
    msg.pose.orientation.x = 0
    msg.pose.orientation.y = -0.7
    msg.pose.orientation.z = 0
    #msg.mode = Pictogram.PICTOGRAM_MODE
    msg.mode = Pictogram.STRING_MODE
    msg.speed = 1.0
    # msg.ttl = 5.0
    msg.size = 1
    msg.color.r = 25 / 255.0
    msg.color.g = 255 / 255.0
    msg.color.b = 240 / 255.0
    msg.color.a = 1.0
    msg.character = pictograms[counter]
    p.publish(msg)
    r.sleep()
    counter = counter + 1
    if len(pictograms) == counter:
        counter = 0
        
    br.sendTransform(
            (0,0,0),
            tf.transformations.quaternion_from_euler(0,0,0),
            rospy.Time.now(),
            'map',
            'base_link'
            )
