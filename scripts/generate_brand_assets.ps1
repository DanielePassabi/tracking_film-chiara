Add-Type -AssemblyName System.Drawing

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent (Split-Path -Parent $PSCommandPath)
$assets = Join-Path $root "site\assets"
$heroPath = Join-Path $assets "polpetta-hero.png"

function New-GradientBitmap {
  param(
    [int]$Width,
    [int]$Height,
    [string]$Text,
    [int]$FontSize,
    [string]$OutPath
  )

  $bitmap = [System.Drawing.Bitmap]::new($Width, $Height)
  $graphics = [System.Drawing.Graphics]::FromImage($bitmap)
  $graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
  $rect = [System.Drawing.Rectangle]::new(0, 0, $Width, $Height)
  $brush = [System.Drawing.Drawing2D.LinearGradientBrush]::new(
    $rect,
    [System.Drawing.Color]::FromArgb(251, 113, 133),
    [System.Drawing.Color]::FromArgb(124, 58, 237),
    35
  )
  $graphics.FillRectangle($brush, $rect)

  $overlay = [System.Drawing.SolidBrush]::new([System.Drawing.Color]::FromArgb(70, 22, 9, 31))
  $graphics.FillRectangle($overlay, $rect)

  $font = [System.Drawing.Font]::new("Segoe UI", $FontSize, [System.Drawing.FontStyle]::Bold, [System.Drawing.GraphicsUnit]::Pixel)
  $format = [System.Drawing.StringFormat]::new()
  $format.Alignment = [System.Drawing.StringAlignment]::Center
  $format.LineAlignment = [System.Drawing.StringAlignment]::Center
  $textBrush = [System.Drawing.SolidBrush]::new([System.Drawing.Color]::FromArgb(255, 247, 255))
  $textRect = [System.Drawing.RectangleF]::new(0, 0, $Width, $Height)
  $graphics.DrawString($Text, $font, $textBrush, $textRect, $format)

  $bitmap.Save($OutPath, [System.Drawing.Imaging.ImageFormat]::Png)
  $graphics.Dispose()
  $bitmap.Dispose()
}

function New-SharePreview {
  param([string]$OutPath)

  $width = 1200
  $height = 630
  $bitmap = [System.Drawing.Bitmap]::new($width, $height)
  $graphics = [System.Drawing.Graphics]::FromImage($bitmap)
  $graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
  $graphics.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::AntiAliasGridFit

  if (Test-Path $heroPath) {
    $hero = [System.Drawing.Image]::FromFile($heroPath)
    $graphics.DrawImage($hero, [System.Drawing.Rectangle]::new(0, 0, $width, $height))
    $hero.Dispose()
  } else {
    $baseBrush = [System.Drawing.Drawing2D.LinearGradientBrush]::new(
      [System.Drawing.Rectangle]::new(0, 0, $width, $height),
      [System.Drawing.Color]::FromArgb(22, 9, 31),
      [System.Drawing.Color]::FromArgb(124, 58, 237),
      25
    )
    $graphics.FillRectangle($baseBrush, 0, 0, $width, $height)
  }

  $shade = [System.Drawing.Drawing2D.LinearGradientBrush]::new(
    [System.Drawing.Rectangle]::new(0, 0, $width, $height),
    [System.Drawing.Color]::FromArgb(238, 18, 7, 29),
    [System.Drawing.Color]::FromArgb(90, 124, 58, 237),
    0
  )
  $graphics.FillRectangle($shade, 0, 0, $width, $height)

  $eyebrowFont = [System.Drawing.Font]::new("Segoe UI", 28, [System.Drawing.FontStyle]::Bold, [System.Drawing.GraphicsUnit]::Pixel)
  $titleFont = [System.Drawing.Font]::new("Segoe UI", 92, [System.Drawing.FontStyle]::Bold, [System.Drawing.GraphicsUnit]::Pixel)
  $bodyFont = [System.Drawing.Font]::new("Segoe UI", 33, [System.Drawing.FontStyle]::Regular, [System.Drawing.GraphicsUnit]::Pixel)
  $pink = [System.Drawing.SolidBrush]::new([System.Drawing.Color]::FromArgb(249, 168, 212))
  $white = [System.Drawing.SolidBrush]::new([System.Drawing.Color]::FromArgb(255, 247, 255))
  $muted = [System.Drawing.SolidBrush]::new([System.Drawing.Color]::FromArgb(218, 214, 224))

  $graphics.DrawString("TV TIME EXPORT", $eyebrowFont, $pink, 72, 98)
  $graphics.DrawString("Polpetta TV", $titleFont, $white, 66, 155)
  $graphics.DrawString("Diary", $titleFont, $white, 66, 252)
  $graphics.DrawString("Serie viste, comfort show e piccoli ritorni speciali.", $bodyFont, $muted, [System.Drawing.RectangleF]::new(74, 392, 700, 110))

  $badgeRect = [System.Drawing.Rectangle]::new(74, 510, 360, 60)
  $badgeBrush = [System.Drawing.SolidBrush]::new([System.Drawing.Color]::FromArgb(210, 249, 168, 212))
  $badgePath = [System.Drawing.Drawing2D.GraphicsPath]::new()
  $diameter = 60
  $badgePath.AddArc($badgeRect.X, $badgeRect.Y, $diameter, $diameter, 90, 180)
  $badgePath.AddArc($badgeRect.Right - $diameter, $badgeRect.Y, $diameter, $diameter, 270, 180)
  $badgePath.CloseFigure()
  $graphics.FillPath($badgeBrush, $badgePath)
  $badgeFont = [System.Drawing.Font]::new("Segoe UI", 24, [System.Drawing.FontStyle]::Bold, [System.Drawing.GraphicsUnit]::Pixel)
  $dark = [System.Drawing.SolidBrush]::new([System.Drawing.Color]::FromArgb(42, 11, 40))
  $graphics.DrawString("137 serie · 6047 episodi", $badgeFont, $dark, 102, 522)

  $bitmap.Save($OutPath, [System.Drawing.Imaging.ImageFormat]::Png)
  $graphics.Dispose()
  $bitmap.Dispose()
}

New-GradientBitmap -Width 192 -Height 192 -Text "P" -FontSize 118 -OutPath (Join-Path $assets "icon-192.png")
New-GradientBitmap -Width 512 -Height 512 -Text "P" -FontSize 315 -OutPath (Join-Path $assets "icon-512.png")
New-GradientBitmap -Width 180 -Height 180 -Text "P" -FontSize 110 -OutPath (Join-Path $assets "apple-touch-icon.png")
New-SharePreview -OutPath (Join-Path $assets "share-preview.png")

Write-Host "Generated brand assets in $assets"
