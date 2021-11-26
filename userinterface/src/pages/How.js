import React from "react";
// import { iframe } from "@chakra-ui/react";

import Hero from "../components/sections/Hero";
import LandingLayout from "../components/layouts/LandingLayout";

export default function how() {
  return (
    <LandingLayout>
      <Hero
        title="Welcome to my Final Project"
        subtitle="Where each computer vision project starts with a smile"
        image="https://source.unsplash.com/collection/1397626/1200x900"
        ctaText="Click Here?"
        ctaLink="/signup"
      />
    </LandingLayout>
  );
}

  // <iframe title = "P5" src="https://editor.p5js.org/JaredGlaub/full/Y0hZKucLW" width="600" height="650">
  // </iframe>