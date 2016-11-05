<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
	<html>
		<head>
			<title>Food Portion Sizes Information</title>
		</head>
		<body>
			<xsl:for-each select="foodPortionSizes/*">
				<xsl:apply-templates/>
			</xsl:for-each>
		</body>
	</html>
</xsl:template>

<xsl:template match="photo">
	<img src="../res/<xsl:value-of select="./photofilename">" />
	<p>Photo Guide Code: <xsl:value-of select="./photoGuideCode"/></p>
	<p>Photo Number: <xsl:value-of select="./photoNumber"/></p>
	<p>Photo Description: <xsl:value-of select="./photoDescription"/></p>
	<table>
		<xsl:for-each select="./photoItem">
			<xsl:apply-templates/>
		</xsl:for-each>
	</table>
</xsl:template>

<xsl:template match="photoItem">
	<tr>
		<td><xsl:value-of select="./inPhotoCode"/></td>
		<td><xsl:value-of select="./atlasNumber"/></td>
		<td><xsl:value-of select="./itemDescription"/></td>
		<td><xsl:value-of select="./weight"/></td>
	</tr>
</xsl:template>