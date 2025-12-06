<?php
require __DIR__. '/vendor/autoload.php';

function vf(string $main) : void{
$count = 0;
 if(is_dir($main) && count($files = scandir($main)) > 0){
foreach($files as $file){
 if(in_array(pathinfo($file, PATHINFO_EXTENSION), ['mp4', 'mov']) && !file_exists($main. pathinfo($file, PATHINFO_FILENAME). '.webm')) { 
  $main2 = $main. $file;
  $ffprobe = FFMpeg\FFProbe::create()->streams($main2)->videos()->first();
  $dm = $ffprobe->getDimensions();
  $settings = [
   'timeout' => 3600,
  ];
  $video = FFMpeg\FFMpeg::create($settings)->open($main2);
  $format = new FFMpeg\Format\Video\WebM(); 
  echo 'Видео '. $file. ' ';
  $previous_percentage = null;
  $format->on('progress', function ($video, $format, $percentage) use (&$previous_percentage) {
    if ($percentage !== $previous_percentage) {
        echo 'сжалось на: ' . $percentage . '%' . "\n";
        $previous_percentage = $percentage;
    }
});
  /*$start = 0;
  $duration = 29;
  $video->filters()->clip(FFMpeg\Coordinate\TimeCode::fromSeconds($start), FFMpeg\Coordinate\TimeCode::fromSeconds($duration));*/
  $height = $dm->getHeight();
  $width = $dm->getWidth();
  if(isset($ffprobe->all()['side_data_list'][0]['rotation']) || $height > $width){
  $video->filters()->resize(new FFMpeg\Coordinate\Dimension($width, $height)); 
  }
  else{
  $video->filters()->resize(new FFMpeg\Coordinate\Dimension($height, $width)); 
  }
  $format->setKiloBitrate(1000);
  $format->setAudioKiloBitrate(128);
  $video->save($format, $main. pathinfo($file, PATHINFO_FILENAME) . '.webm');
  //unlink($main2);
  $count++;
 }
  }
   }
  echo 'Видео отредактировано: '. $count. '.'. "\n";
}
vf($_SERVER['argv'][1]. '/Видео/');
?>
