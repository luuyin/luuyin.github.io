---
layout: page
permalink: /CV/
title: CV
# description: Materials for courses you taught. Replace this text with your description.
nav: true
nav_order: 2
---


[Full CV Download Here](/assets/pdf/CV-Ph.D.pdf).

<html>
  <head>
     <style>

        @page{
        size: letter portrait;
        margin: 0;
        }

        *{
        box-sizing: border-box;
        }

        :root{
        --page-height: 20in;

        --main-width: 9in;
        --sidebar-width: calc(var(--page-width) - var(--main-width));
        --decorator-horizontal-margin: 0.2in;

        --sidebar-horizontal-padding: 0.2in;

        /* XXX: using px for very good precision control */
        --decorator-outer-offset-top: 10px;
        --decorator-outer-offset-left: -5.5px;
        --decorator-border-width: 1px;
        --decorator-outer-dim: 9px;
        --decorator-border: 1px solid #ccc;

        --row-blocks-padding-top: 5pt;
        --date-block-width: 0.6in;

        --main-blocks-title-icon-offset-left: -19pt;
        }

        body{
        width: var(--page-width);
        height: var(--page-height);
        margin: 0;
        font-family: "Open Sans", sans-serif; 
        font-weight: 300;
        line-height: 2;
        color: #444;
        hyphens: auto;
        }

        h1, h2, h3{
        margin: 0;
        color: #000;
        }

        li{
        list-style-type: none;
        }

        #main{
        float: left;
        width: var(--main-width);
        padding: 0.25in 0.25in 0 0.25in;
        font-size: 10pt;
        }

        #sidebar{
        float: right;
        position: relative; /* for disclaimer */
        width: var(--sidebar-width);
        height: 100%;
        padding: 0.6in var(--sidebar-horizontal-padding);
        background-color: #f2f2f2;
        font-size: 8.5pt;
        }

        /* main */

        /** big title **/
        #title, h1, h2{
        text-transform: uppercase;
        }

        #title{
        position: relative;
        left: 0.55in;
        margin-bottom: 0.3in;
        line-height: 10;
        }

        #title h1{
        font-weight: 300;
        font-size: 18pt;
        line-height: 1.5;
        }

        #title h1 strong{
        margin: auto 2pt auto 4pt;
        font-weight: 600;
        }

        .subtitle{
        font-size: 8pt;
        }

        /*** categorial blocks ***/

        .main-block{
        margin-top: 0.1in;
        }

        #main h2{
        position: relative;
        top: var(--row-blocks-padding-top);
        /* XXX: 0.5px for aligning fx printing */
        left: calc((var(--date-block-width) + var(--decorator-horizontal-margin)));
        font-weight: 400;
        font-size: 14pt;
        color: #555;
        }

        #main h2 > i{
        /* use absolute position to prevent icon's width from misaligning title */
        /* assigning a fixed width here is no better due to needing to align decorator
            line too */
        position: absolute;
        left: var(--main-blocks-title-icon-offset-left);
        z-index: 1; /* over decorator line */
        color: #444;
        }

        #main h2::after{ /* extends the decorator line */
        height: calc(var(--row-blocks-padding-top) * 2);
        position: relative;
        top: calc(-1 * var(--row-blocks-padding-top));
        /* XXX: 0.5px for aligning fx printing */
        left: calc(-1 * var(--decorator-horizontal-margin));
        display: block;
        border-left: var(--decorator-border);
        z-index: 0;
        line-height: 0;
        font-size: 0;
        content: ' ';
        }

        /**** minor tweaks on the icon fonts ****/
        #main h2 > .fa-graduation-cap{
        left: calc(var(--main-blocks-title-icon-offset-left) - 2pt);
        top: 2pt;
        }

        #main h2 > .fa-suitcase{
        top: 1pt;
        }

        #main h2 > .fa-folder-open{
        top: 1.5pt;
        }

        /**** individual row blocks (date - decorator - details) ****/

        .blocks{
        display: flex;
        flex-flow: row nowrap;
        }

        .blocks > div{
        padding-top: var(--row-blocks-padding-top);
        }

        .date{
        flex: 0 0 var(--date-block-width);
        padding-top: calc(var(--row-blocks-padding-top) + 2.5pt) !important;
        padding-right: var(--decorator-horizontal-margin);
        font-size: 10pt;
        text-align: right;
        line-height: 1;
        }

        .date span{
        display: block;
        }

        .date span:nth-child(2)::before{
        position: relative;
        top: 1pt;
        right: 5.5pt;
        display: block;
        height: 15pt;
        content: '|';
        }

        .decorator{
        flex: 0 0 0;
        position: relative;
        width: 2pt;
        min-height: 100%;
        border-left: var(--decorator-border);
        }

        /*
        * XXX: Use two filled circles to achieve the circle-with-white-border effect.
        * The normal technique of only using one pseudo element and
        * border: 1px solid white; style makes firefox erroneously either:
        * 1) overflows the grayshade background (if no background-clip is set), or
        * 2) shows decorator line which should've been masked by the white border
        *
        */

        .decorator::before{
        position: absolute;
        top: var(--decorator-outer-offset-top);
        left: var(--decorator-outer-offset-left);
        content: ' ';
        display: block;
        width: var(--decorator-outer-dim);
        height: var(--decorator-outer-dim);
        border-radius: calc(var(--decorator-outer-dim) / 2);
        background-color: #fff;
        }

        .decorator::after{
        position: absolute;
        top: calc(var(--decorator-outer-offset-top) + var(--decorator-border-width));
        left: calc(var(--decorator-outer-offset-left) + var(--decorator-border-width));
        content: ' ';
        display: block;
        width: calc(var(--decorator-outer-dim) - (var(--decorator-border-width) * 2));
        height: calc(var(--decorator-outer-dim) - (var(--decorator-border-width) * 2));
        border-radius: calc((var(--decorator-outer-dim) - (var(--decorator-border-width) * 2)) / 2);
        background-color: #555;
        }

        .blocks:last-child .decorator{ /* slightly shortens it */
        margin-bottom: 0.25in;
        }

        /***** fine-tunes on the details block where the real juice is *****/

        .details{
        flex: 1 0 0;
        padding-left: var(--decorator-horizontal-margin);
        padding-top: calc(var(--row-blocks-padding-top) - 0.5pt) !important; /* not sure why but this is needed for better alignment */
        }

        .details header{
        color: #000;
        }

        .details h3{
        font-size: 13pt; 
        font-weight: 500;
        }

        .main-block:not(.concise) .details div{
        margin: 0.18in 0 0.1in 0; 
        }

        .main-block:not(.concise) .blocks:last-child .details div{
        margin-bottom: 0;
        }

        .main-block.concise .details div:not(.concise){
        /* use padding to work around the fact that margin doesn't affect floated
            neighboring elements */
        padding: 0.05in 0 0.07in 0;
        }

        .details .place{ 
        float: left;
        font-size: 11pt;
        }

        .details .location{
        float: right;

        }

        .details div{
        clear: both;
        }

        .details .location::before{
        display: inline-block;
        position: relative;
        right: 3pt;
        top: 0.25pt;
        font-family: FontAwesome;
        font-weight: normal;
        font-style: normal;
        text-decoration: inherit;
        content: "\f041";
        }

        /***** fine-tunes on the lists... *****/

        #main ul{
        padding-left: 0.07in;
        margin: 0.08in 0;
        }

        #main li{
        margin: 0 0 0.025in 0;
        }

        /****** customize list symbol style ******/
        #main li::before{
        position: relative;
        margin-left: -4.25pt;
        content: '• ';
        }

        .details .concise ul{
        margin: 0 !important;
        -webkit-columns: 2;
        -moz-columns: 2;
        columns: 2;
        }

        .details .concise li{
        margin: 0 !important;
        }

        .details .concise li{
        margin-left: 0 !important;
        }



        /* sidebar */

        #sidebar h1{
        font-weight: 400;
        font-size: 11pt;
        }

        .side-block{
        margin-top: 0.5in; 
        }

        #contact ul{
        margin-top: 0.05in;
        padding-left: 0;
        font-family: "Source Code Pro";
        font-weight: 400;
        line-height: 1.75;
        }

        #contact li > i{
        width: 9pt; /* for text alignment */
        text-align: right;
        }

        #skills{
        line-height: 1.5;
        }

        #skills ul{
        margin: 0.05in 0 0.15in;
        padding: 0;
        }

        #disclaimer{
        position: absolute;
        bottom: var(--sidebar-horizontal-padding);
        right: var(--sidebar-horizontal-padding);
        font-size: 7.5pt;
        font-style: italic;
        line-height: 1.1;
        text-align: right;
        color: #777;
        }

        #disclaimer code{
        color: #666;
        font-family: "Source Code Pro";
        font-weight: 400;
        font-style: normal;
        }





     </style>

















     
  </head>
  <body lang="en">
    <section id="main">
    
      <section class="main-block concise">
        <h2>
          <i class="fa fa-graduation-cap"></i> Education
        </h2>
        <section class="blocks">
          <div class="date">
            <span>10.2018</span><span>Present</span>
          </div>
          <div class="decorator">
          </div>
          <div class="details">
            <header>
              <h3>Ph.D. in Computer Science.</h3>
              <span class="place">Eindhoven University of Technology</span>
              <span class="location">Eindhoven, Netherlands</span>
            </header>
            <div>Department: Mathematics and Computer Science
            <br> Specialization: Sparse Training, Knowledge Elicitation and Presentation, MetricLearning, Few-shot learning, Active Learning
            <br> Promotors: Prof. Dr. Mykola Pechenizkiy; Dr. Vlado Menkovski
            </div>
          </div>
        </section>


        <section class="blocks">
          <div class="date">
            <span>09.2015</span><span>07.2018</span>
          </div>
          <div class="decorator">
          </div>
          <div class="details">
            <header>
              <h3>M.Eng C. in Control Engineering.</h3>
              <span class="place">Harbin Institute of Technology Shenzhen GraduateSchool</span>
              <span class="location">Shenzhen, China</span>
            </header>
            <div>Department: Mechanical Engineering and Automation
            <br> Specialization: Control Engineering, Robotics
            <br> Promotors: Prof. Dr. Xiaorui Zhu
            </div>
          </div>
        </section>



        <section class="blocks">
          <div class="date">
            <span>09.2009</span><span>07.2013</span>
          </div>
          <div class="decorator">
          </div>
          <div class="details">
            <header>
              <h3>B.Eng in Electrical Engineering and Automation</h3>
              <span class="place">Harbin Institute of Technology</span>
              <span class="location">China</span>
            </header>
            <div>Department: nformation and Electrical Engineering
            </div>
          </div>
        </section>

        
      </section>


      <section class="main-block">
        <h2>
          <i class="fa fa-suitcase"></i> Experiences
        </h2>
        <section class="blocks">
          <div class="date">
            <span>2015</span><span>present</span>
          </div>
          <div class="decorator">
          </div>
          <div class="details">
            <header>
              <h3>Some Position</h3>
              <span class="place">Some Workplace</span>
              <span class="location">(remote)</span>
            </header>
            <div>
              <ul>
                <li>Lorem ipsum dolor sit amet, consectetur adipiscing elit</li>
                <li>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin nec mi ante. Etiam odio eros, placerat eu metus id, gravida eleifend odio. Vestibulum dapibus pharetra odio, egestas ullamcorper ipsum congue ac. Maecenas viverra tortor eget convallis vestibulum. Donec pulvinar venenatis est, non sollicitudin metus laoreet sed. Fusce tincidunt felis nec neque aliquet porttitor</li>
              </ul>
              </div>
          </div>
        </section>
        <section class="blocks">
          <div class="date">
            <span>2014</span><span>2015</span>
          </div>
          <div class="decorator">
          </div>
          <div class="details">
            <header>
              <h3>Another Position</h3>
              <span class="place">Some Workplace</span>
              <span class="location">Some City, Some Country</span>
            </header>
            <div>
              <ul>
                <li>Lorem ipsum dolor sit amet, consectetur adipiscing elit</li>
                <li>Lorem ipsum dolor sit amet, consectetur adipiscing elit</li>
                <li>Lorem ipsum dolor sit amet, consectetur adipiscing elit</li>
              </ul>
            </div>
          </div>
        </section>
        <section class="blocks">
          <div class="date">
            <span>2013</span><span>2014</span>
          </div>
          <div class="decorator">
          </div>
          <div class="details">
            <header>
              <h3>Yet Another Job Position</h3>
              <span class="place">Some Workplace</span>
              <span class="location">Some City, Some Country</span>
            </header>
            <div>
              <ul>
                <li>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin nec mi ante. Etiam odio eros, placerat eu metus id, gravida eleifend odio</li>
                <li>Lorem ipsum dolor sit amet, consectetur adipiscing elit</li>
              </ul>
              </div>
          </div>
        </section>
      </section>
      <section class="main-block">
        <h2>
          <i class="fa fa-folder-open"></i> Selected Projects
        </h2>
        <section class="blocks">
          <div class="date">
            <span>2015</span><span>2016</span>
          </div>
          <div class="decorator">
          </div>
          <div class="details">
            <header>
              <h3>Some Project 1</h3>
              <span class="place">Some workplace</span>
            </header>
            <div>n Forty-Two Discover
              <ul>
                <li>Lorem ipsum dolor sit amet, consectetur adipiscing elit</li>
                <li>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin nec mi ante. Etiam odio eros, placerat eu metus id, gravida eleifend odio. Vestibulum dapibus pharetra odio, egestas ullamcorper ipsum congue ac</li>
                <li>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin nec mi ante. Etiam odio eros, placerat eu metus id, gravida eleifend odio</li>
              </ul>
            </div>
          </div>
        </section>
        <section class="blocks">
          <div class="date">
            <span>2014</span><span>2015</span>
          </div>
          <div class="decorator">
          </div>
          <div class="details">
            <header>
              <h3>Some Project 2</h3>
              <span class="place">Some workplace</span>
            </header>
            <div>
              <ul>
                <li>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin nec mi ante. Etiam odio eros, placerat eu metus id, gravida eleifend odio. Vestibulum dapibus pharetra odio, egestas ullamcorper ipsum congue ac. Maecenas viverra tortor eget convallis vestibulum. Donec pulvinar venenatis est, non sollicitudin metus laoreet sed. Fusce tincidunt felis nec neque aliquet porttitor</li>
              </ul>
            </div>
          </div>
        </section>
        <section class="blocks">
          <div class="date">
            <span>2014</span>
          </div>
          <div class="decorator">
          </div>
          <div class="details">
            <header>
              <h3>Some Project 3</h3>
              <span class="place">Some workplace</span>
            </header>
            <div>
              <ul>
                <li>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin nec mi ante. Etiam odio eros, placerat eu metus id, gravida eleifend odio</li>
              </ul>
            </div>
          </div>
        </section>
      </section>

      
      <section class="main-block concise">
        <h2>
          <i class="fa fa-graduation-cap"></i> Education
        </h2>
        <section class="blocks">
          <div class="date">
            <span>10.2018</span><span>Present</span>
          </div>
          <div class="decorator">
          </div>
          <div class="details">
            <header>
              <h3>Ph.D. in Computer Science.</h3>
              <span class="place">Eindhoven University of Technology</span>
              <span class="location">Eindhoven, Netherlands</span>
            </header>
            <div>Department: Mathematics and Computer Science
            <br> Specialization: Sparse Training, Knowledge Elicitation and Presentation, MetricLearning, Few-shot learning, Active Learning
            <br> Promotors: Prof. Dr. Mykola Pechenizkiy; Dr. Vlado Menkovski
            </div>
          </div>
        </section>


        <section class="blocks">
          <div class="date">
            <span>09.2015</span><span>07.2018</span>
          </div>
          <div class="decorator">
          </div>
          <div class="details">
            <header>
              <h3>M.Eng C. in Control Engineering.</h3>
              <span class="place">Harbin Institute of Technology Shenzhen GraduateSchool</span>
              <span class="location">Shenzhen, China</span>
            </header>
            <div>Department: Mechanical Engineering and Automation
            <br> Specialization: Control Engineering, Robotics
            <br> Promotors: Prof. Dr. Xiaorui Zhu
            </div>
          </div>
        </section>



        <section class="blocks">
          <div class="date">
            <span>09.2009</span><span>07.2013</span>
          </div>
          <div class="decorator">
          </div>
          <div class="details">
            <header>
              <h3>B.Eng in Electrical Engineering and Automation</h3>
              <span class="place">Harbin Institute of Technology</span>
              <span class="location">China</span>
            </header>
            <div>Department: nformation and Electrical Engineering
            </div>
          </div>
        </section>

        
      </section>
    </section>



  </body>
</html>