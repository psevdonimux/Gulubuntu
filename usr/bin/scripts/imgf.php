<?php
function imgf(string $main) : void {
    $count = 0;
    $divider = 1;
    if (is_dir($main) && count($files = scandir($main)) > 0) {
        foreach ($files as $file) {
            $format = pathinfo($file, PATHINFO_EXTENSION);
            if (in_array($format, ['png', 'jpg', 'jpeg', 'heif']) && !file_exists($main. pathinfo($file, PATHINFO_FILENAME). '.webp')){ 
                $main2 = $main . $file;               
                if ($format === 'heif') {
                    $outputFile = $main . pathinfo($file, PATHINFO_FILENAME) . '.jpg'; 
                    exec("heif-convert ". $main2. ' '. $outputFile);
                    $format = 'jpg';
                    $main2 = $main . pathinfo($file, PATHINFO_FILENAME). '.jpg';
                }
                $img = match($format) {
                    'png' => imagecreatefrompng($main2),
                    'jpg', 'jpeg' => imagecreatefromjpeg($main2),
                };
                $size = getimagesize($main2);
                imagepalettetotruecolor($img);
                imagecolortransparent($img, imagecolorallocate($img, 0, 0, 0));
                imagewebp(imagescale($img, ceil($size[0] / $divider), ceil($size[1] / $divider)), $main . pathinfo($file, PATHINFO_FILENAME) . '.webp', 50);       
                $count++;
               }         
        }
    }
  echo 'Изображений отредактировано: '. $count. '.'. "\n";
}
imgf($_SERVER['argv'][1]. '/Изображения/');
?>
