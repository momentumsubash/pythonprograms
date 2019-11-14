<!-- #thi is just a simple change  -->  


    <!-- Slide -->



                                <div  class="test_slider_item text-center">

                                    <div class="rating rating_{{$val->star}} d-flex flex-row align-items-start justify-content-center"><i></i><i></i><i></i><i></i><i></i></div>

                                    <div class="testimonial_title"><a href="#">{{$val->title}}</a></div>

                                    <div class="testimonial_text">

                                        <p>{{$val->message}}</p>

                                    </div>
                                    <div class="testimonial_image"><img src="{{$val->profile_image}}" alt=""></div>

                                    <div class="testimonial_author"><a href="#">{{$val->person_name}}</a>, {{$val->address}}</div>

{{--                                        <div class="testimonial_title"><a href="#">{{$val->title}}</a></div>--}}
{{--                                        <div class="testimonial_text">{{$val->message}}</div>--}}
{{--                                        <div class="testimonial_image"><img src="images/user_1.jpg" alt=""></div>--}}
{{--                                        <div class="testimonial_author"><a href="#">{{$val->fullname}}</a>, {{$val->address}}</div>--}}



                                </div>

                                @endforeach